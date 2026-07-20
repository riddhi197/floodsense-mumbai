// Detect environment and set API Base URL
const API_BASE = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' || window.location.protocol === 'file:' 
    ? 'http://127.0.0.1:8000' 
    : '';

let currentScope = 'mumbai';

// Tab switching logic
function switchTab(tabId) {
    // Hide all sections
    document.querySelectorAll('main > div > section').forEach(section => {
        section.classList.add('hidden');
    });
    // Show active section
    document.getElementById(`tab-${tabId}`).classList.remove('hidden');

    // Reset button states
    document.querySelectorAll('aside nav button').forEach(btn => {
        btn.classList.remove('bg-water', 'text-white');
        btn.classList.add('text-inkSoft', 'hover:bg-waterTint', 'hover:text-ink');
    });
    // Highlight active button
    const activeBtn = document.getElementById(`btn-${tabId}`);
    activeBtn.classList.remove('text-inkSoft', 'hover:bg-waterTint', 'hover:text-ink');
    activeBtn.classList.add('bg-water', 'text-white');

    // Update Header
    const titles = {
        dashboard: { t: "Dashboard Overview", d: "Real-time flood intelligence and predictive risk telemetry" },
        predictor: { t: "Flood Severity Predictor", d: "Test what-if precipitation and antecedent soil scenarios on AI models" },
        wards: { t: "Ward Risk Profiler", d: "Gaussian Mixture Model (GMM) ward clustering and vulnerability profiles" },
        insights: { t: "Data Insights & EDA", d: "Interactive visual exploratory analysis of monsoon historical dataset" },
        news: { t: "News & Media NLP Analysis", d: "Independent news scraping validation feed and timeline index" },
        economic: { t: "Economic Loss Simulator", d: "Simulate productivity loss and transit delays across severity categories" }
    };
    document.getElementById('header-title').innerText = titles[tabId].t;
    document.getElementById('header-desc').innerText = titles[tabId].d;

    // Load data when tab opens
    if (tabId === 'wards') loadWards();
    if (tabId === 'news') loadNews();
    if (tabId === 'insights') loadInsights();
}

// Update value slider text labels
function updateVal(type) {
    const val = document.getElementById(`input-${type}`).value;
    const txt = document.getElementById(`val-${type}`);
    if (type === 'rain') txt.innerText = `${val}.0 mm`;
    if (type === 'rain3d') txt.innerText = `${val}.0 mm`;
    if (type === 'rain7d') txt.innerText = `${val}.0 mm`;
    if (type === 'hours') txt.innerText = `${parseFloat(val).toFixed(1)} hrs`;
    if (type === 'month') {
        const months = {6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October'};
        txt.innerText = `${months[val]} (${val})`;
    }
}

// Set model scope
function setScope(scope) {
    currentScope = scope;
    const btnM = document.getElementById('scope-mumbai');
    const btnK = document.getElementById('scope-konkan');

    if (scope === 'mumbai') {
        btnM.className = "p-4 rounded-md border-2 border-water bg-waterTint text-ink font-semibold transition-all duration-150";
        btnK.className = "p-4 rounded-md border-2 border-mist bg-paper text-inkSoft hover:text-ink transition-all duration-150";
    } else {
        btnK.className = "p-4 rounded-md border-2 border-water bg-waterTint text-ink font-semibold transition-all duration-150";
        btnM.className = "p-4 rounded-md border-2 border-mist bg-paper text-inkSoft hover:text-ink transition-all duration-150";
    }
}

// Run prediction model inference
async function runInference() {
    const reqData = {
        scope: currentScope,
        rain_today: parseFloat(document.getElementById('input-rain').value),
        rain_3d: parseFloat(document.getElementById('input-rain3d').value),
        rain_7d: parseFloat(document.getElementById('input-rain7d').value),
        rain_hours: parseFloat(document.getElementById('input-hours').value),
        month_val: parseInt(document.getElementById('input-month').value)
    };

    const resDiv = document.getElementById('prediction-result');
    resDiv.classList.remove('hidden');
    resDiv.innerHTML = `<span class="eyebrow">Inference Results</span><div class="text-inkSoft font-mono animate-pulse mt-2">Executing ML model inference API...</div>`;

    try {
        const response = await fetch(`${API_BASE}/api/predict`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(reqData)
        });
        const data = await response.json();

        // Field-report palette per risk category
        let bannerColor = "bg-safeTint border-safe text-safe";
        let barColor = "#2E7D5B";
        let stampClass = "border-safe text-safe bg-safeTint";
        if (data.category === "Slight") {
            bannerColor = "bg-amberTint border-amber text-amber";
            barColor = "#B9791A";
            stampClass = "border-amber text-amber bg-amberTint";
        } else if (data.category === "Moderate") {
            bannerColor = "bg-amberTint border-flood/60 text-flood";
            barColor = "#C1631F";
            stampClass = "border-flood/60 text-flood bg-amberTint";
        } else if (data.category === "Severe") {
            bannerColor = "bg-floodTint border-flood text-flood";
            barColor = "#A83B2C";
            stampClass = "border-flood text-flood bg-floodTint";
        }

        const probPct = (data.probability * 100).toFixed(1);

        resDiv.innerHTML = `
            <span class="eyebrow">Inference Results (${data.scope === 'mumbai' ? 'Mumbai Model' : 'Konkan Stacking Model'})</span>
            <div class="p-6 rounded-md border ${bannerColor} flex flex-col gap-3 mt-2">
                <span class="stamp ${stampClass} w-fit">${data.category.toUpperCase().replace('_', ' ')} LIMIT</span>
                <p class="text-sm font-medium text-ink leading-relaxed">${data.description}</p>
            </div>
            <div class="space-y-2 mt-4">
                <div class="flex justify-between text-sm font-semibold">
                    <span class="text-ink">Flood Event Probability Score</span>
                    <span class="font-mono text-water">${probPct}%</span>
                </div>
                <div class="w-full bg-mist h-3 rounded-full overflow-hidden">
                    <div class="h-full transition-all duration-500" style="width: ${probPct}%; background-color: ${barColor}"></div>
                </div>
            </div>
        `;
    } catch (e) {
        resDiv.innerHTML = `<span class="eyebrow">Inference Results</span><div class="text-flood font-medium mt-2">Failed to execute prediction: ${e.message}</div>`;
    }
}

// Fetch GMM Wards Risk index
async function loadWards() {
    const container = document.getElementById('wards-container');
    try {
        const response = await fetch(`${API_BASE}/api/wards`);
        const data = await response.json();

        container.innerHTML = '';
        data.forEach(w => {
            // Support both PostgreSQL (lowercase) and SQLite (capitalized) keys
            const risk_level = w.Risk_Level || w.risk_level || 'Low';
            const ward_code = w.Ward_Code || w.ward_code || '';
            const area_covered = w.Area_Covered || w.area_covered || '';
            const known_spots = w.Known_Flood_Spots_Count !== undefined ? w.Known_Flood_Spots_Count : w.known_flood_spots_count;
            const pop_pct = w.Population_At_Risk_Pct !== undefined ? w.Population_At_Risk_Pct : w.population_at_risk_pct;
            const cluster_label = w.Cluster_Label || w.cluster_label || '';

            let borderColor = 'border-water';
            let badgeClass = 'bg-waterTint text-water';
            if (risk_level === 'High') { borderColor = 'border-flood'; badgeClass = 'bg-floodTint text-flood'; }
            if (risk_level === 'Medium') { borderColor = 'border-amber'; badgeClass = 'bg-amberTint text-amber'; }

            container.innerHTML += `
                <div class="p-5 rounded-md bg-card border border-mist border-l-4 ${borderColor} flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-center mb-2">
                            <span class="font-semibold text-ink">Ward ${ward_code}</span>
                            <span class="text-xs font-semibold px-2.5 py-1 rounded-full font-mono ${badgeClass}">${risk_level.toUpperCase()} RISK</span>
                        </div>
                        <h4 class="eyebrow mb-3">${area_covered}</h4>
                        <div class="text-sm space-y-1.5 text-inkSoft font-mono">
                            <div class="flex justify-between"><span>Known Flood Spots:</span> <span class="font-semibold text-ink">${known_spots}</span></div>
                            <div class="flex justify-between"><span>Population at Risk:</span> <span class="font-semibold text-ink">${pop_pct}%</span></div>
                            <div class="flex justify-between"><span>GMM Cluster Group:</span> <span class="font-semibold text-ink">${cluster_label}</span></div>
                        </div>
                    </div>
                </div>
            `;
        });
    } catch (e) {
        container.innerHTML = `<div class="text-flood font-medium">Failed to load ward vulnerability details: ${e.message}</div>`;
    }
}

// Fetch NLP News timeline and cards
async function loadNews() {
    const grid = document.getElementById('news-grid');
    try {
        const response = await fetch(`${API_BASE}/api/news`);
        const data = await response.json();

        // Normalize keys
        const normalizedData = data.map(n => ({
            related_date: n.Related_Date || n.related_date || '',
            severity_score: n.Severity_Score !== undefined ? n.Severity_Score : (n.severity_score !== undefined ? n.severity_score : 0),
            snippet_preview: n.Snippet_Preview || n.snippet_preview || '',
            keywords_found: n.Keywords_Found || n.keywords_found || ''
        }));

        // 1. Render timeline chart
        const sortedData = [...normalizedData].sort((a, b) => new Date(a.related_date) - new Date(b.related_date));
        const dates = sortedData.map(d => d.related_date);
        const scores = sortedData.map(d => d.severity_score);
        const snippets = sortedData.map(d => d.snippet_preview);

        const trace = {
            x: dates,
            y: scores,
            mode: 'markers+lines',
            type: 'scatter',
            text: snippets,
            marker: {
                size: scores.map(s => s * 2.5),
                color: scores,
                colorscale: [[0, '#0B6E7A'], [0.5, '#B9791A'], [1, '#A83B2C']],
                line: { width: 1, color: '#17242B' }
            },
            line: { color: 'rgba(23,36,43,0.15)' }
        };

        const layout = {
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
            font: { color: '#17242B', family: 'IBM Plex Sans' },
            xaxis: { gridcolor: '#B7C1BB', linecolor: '#B7C1BB' },
            yaxis: { gridcolor: '#B7C1BB', linecolor: '#B7C1BB', range: [0, 16] },
            margin: { t: 20, b: 40, l: 40, r: 20 }
        };

        Plotly.newPlot('chart-timeline', [trace], layout, { responsive: true, displayModeBar: false });

        // 2. Render Cards
        grid.innerHTML = '';
        normalizedData.forEach(n => {
            let badgeColor = "bg-waterTint text-water border border-water/20";
            let border = "border-l-water";
            if (n.severity_score >= 10) {
                badgeColor = "bg-floodTint text-flood border border-flood/20";
                border = "border-l-flood";
            } else if (n.severity_score >= 5) {
                badgeColor = "bg-amberTint text-amber border border-amber/20";
                border = "border-l-amber";
            }

            const keyBadges = n.keywords_found.split(',')
                .map(k => k.trim())
                .filter(k => k)
                .map(k => `<span class="bg-paper text-inkSoft text-[10px] font-mono px-2 py-0.5 rounded-md border border-mist">${k}</span>`)
                .join(' ');

            grid.innerHTML += `
                <div class="p-5 rounded-md bg-card border border-mist border-l-4 ${border} flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-center mb-3">
                            <span class="text-xs text-inkSoft font-mono font-semibold">${n.related_date}</span>
                            <span class="text-xs font-semibold px-2 py-0.5 rounded font-mono ${badgeColor}">Score: ${n.severity_score}</span>
                        </div>
                        <p class="text-sm font-medium italic text-ink leading-relaxed mb-4">"${n.snippet_preview}"</p>
                    </div>
                    <div class="border-t border-mist pt-3">
                        <div class="eyebrow mb-1.5">Extracted Tags</div>
                        <div class="flex flex-wrap gap-1">${keyBadges}</div>
                    </div>
                </div>
            `;
        });

    } catch (e) {
        grid.innerHTML = `<div class="text-flood font-medium">Failed to load media NLP news timeline feed: ${e.message}</div>`;
    }
}

// Fetch daily rainfall and render EDA charts
async function loadInsights() {
    try {
        const response = await fetch(`${API_BASE}/api/historical`);
        const data = await response.json();

        // Normalize keys
        const cleanData = data.map(d => ({
            month: d.Month !== undefined ? d.Month : (d.month !== undefined ? d.month : 7),
            rainfall_mm: d.Rainfall_mm !== undefined ? d.Rainfall_mm : (d.rainfall_mm !== undefined ? d.rainfall_mm : 0.0),
            rainfall_3day: d.Rainfall_3day !== undefined ? d.Rainfall_3day : (d.rainfall_3day !== undefined ? d.rainfall_3day : 0.0),
            rainfall_7day: d.Rainfall_7day !== undefined ? d.Rainfall_7day : (d.rainfall_7day !== undefined ? d.rainfall_7day : 0.0),
            confirmed_event: d.Confirmed_Event !== undefined ? d.Confirmed_Event : (d.confirmed_event !== undefined ? d.confirmed_event : 0)
        }));

        // 1. Monthly Box Plot
        const months = {6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October'};
        const boxData = {};
        cleanData.forEach(d => {
            const mName = months[d.month];
            if (!boxData[mName]) boxData[mName] = [];
            boxData[mName].push(d.rainfall_mm);
        });

        const boxTraces = Object.keys(boxData).map(m => ({
            y: boxData[m],
            name: m,
            type: 'box',
            boxpoints: 'outliers',
            marker: { color: m === 'July' ? '#A83B2C' : '#0B6E7A' }
        }));

        Plotly.newPlot('chart-month', boxTraces, {
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
            font: { color: '#17242B', family: 'IBM Plex Sans' },
            xaxis: { gridcolor: '#B7C1BB', linecolor: '#B7C1BB' },
            yaxis: { gridcolor: '#B7C1BB', linecolor: '#B7C1BB', title: 'Rainfall (mm)' },
            margin: { t: 20, b: 40, l: 50, r: 20 }
        }, { responsive: true, displayModeBar: false });

        // 2. Scatter Plot: Intensity vs Saturation
        const normalDays = cleanData.filter(d => d.confirmed_event === 0);
        const floodDays = cleanData.filter(d => d.confirmed_event === 1);

        const traceNormal = {
            x: normalDays.map(d => d.rainfall_mm),
            y: normalDays.map(d => d.rainfall_7day),
            mode: 'markers',
            name: 'Normal Day',
            type: 'scatter',
            marker: { color: '#0B6E7A', size: 6, opacity: 0.55 }
        };

        const traceFlood = {
            x: floodDays.map(d => d.rainfall_mm),
            y: floodDays.map(d => d.rainfall_7day),
            mode: 'markers',
            name: 'Verified Flood Event',
            type: 'scatter',
            marker: { color: '#A83B2C', size: 10, line: { width: 1, color: '#17242B' } }
        };

        Plotly.newPlot('chart-scatter', [traceNormal, traceFlood], {
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
            font: { color: '#17242B', family: 'IBM Plex Sans' },
            xaxis: { gridcolor: '#B7C1BB', linecolor: '#B7C1BB', title: 'Precipitation Intensity Today (mm)' },
            yaxis: { gridcolor: '#B7C1BB', linecolor: '#B7C1BB', title: '7-Day Soil Saturation (mm)' },
            margin: { t: 20, b: 45, l: 50, r: 20 }
        }, { responsive: true, displayModeBar: false });

        // 3. Correlation Heatmap
        const getMean = arr => arr.reduce((a,b)=>a+b,0)/arr.length;
        const getStd = (arr, mean) => Math.sqrt(arr.reduce((a,b)=>a+Math.pow(b-mean,2),0)/(arr.length-1));
        const getCorr = (x, y) => {
            const mx = getMean(x);
            const my = getMean(y);
            const sx = getStd(x, mx);
            const sy = getStd(y, my);
            let sum = 0;
            for(let i=0; i<x.length; i++) {
                sum += (x[i]-mx)*(y[i]-my);
            }
            return sum/((x.length-1)*sx*sy);
        };

        const r = cleanData.map(d => d.rainfall_mm);
        const r3 = cleanData.map(d => d.rainfall_3day);
        const r7 = cleanData.map(d => d.rainfall_7day);

        const matrix = [
            [1.0, getCorr(r, r3), getCorr(r, r7)],
            [getCorr(r3, r), 1.0, getCorr(r3, r7)],
            [getCorr(r7, r), getCorr(r7, r3), 1.0]
        ];

        const zValues = matrix.map(row => row.map(v => parseFloat(v.toFixed(3))));

        const traceHeat = {
            z: zValues,
            x: ['Daily Rain', '3-Day Antecedent', '7-Day Antecedent'],
            y: ['Daily Rain', '3-Day Antecedent', '7-Day Antecedent'],
            type: 'heatmap',
            colorscale: [[0, '#F8E6E2'], [0.5, '#F1F3EE'], [1, '#0B6E7A']],
            zmin: -1, zmax: 1
        };

        Plotly.newPlot('chart-corr', [traceHeat], {
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
            font: { color: '#17242B', family: 'IBM Plex Sans' },
            margin: { t: 20, b: 40, l: 100, r: 20 }
        }, { responsive: true, displayModeBar: false });

    } catch (e) {
        console.error("Failed to render insights: ", e);
    }
}

// Run economic impact simulator logic
function runEconomicSim() {
    const sev = document.getElementById('eco-severity').value;
    const lossEl = document.getElementById('eco-loss');
    const delayEl = document.getElementById('eco-delay');

    if (sev === "No_Flood") {
        lossEl.innerText = "₹0.0 Crores";
        delayEl.innerText = "0 Minutes";
    } else if (sev === "Slight") {
        lossEl.innerText = "₹50.0 Crores";
        delayEl.innerText = "30 Minutes";
    } else if (sev === "Moderate") {
        lossEl.innerText = "₹180.0 Crores";
        delayEl.innerText = "75 Minutes";
    } else {
        lossEl.innerText = "₹480.0 Crores";
        delayEl.innerText = "180 Minutes (3 hrs)";
    }
}

// Refresh data helper
function refreshData() {
    const activeSection = document.querySelector('main > div > section:not(.hidden)');
    const id = activeSection.id.replace('tab-', '');
    if (id === 'wards') loadWards();
    if (id === 'news') loadNews();
    if (id === 'insights') loadInsights();
}

// Initial load triggers
window.onload = () => {
    switchTab('dashboard');
    runEconomicSim();
};
