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
        btn.classList.remove('bg-blue-600', 'text-white', 'shadow-lg', 'shadow-blue-500/10');
        btn.classList.add('text-slate-400', 'hover:bg-slate-800/40', 'hover:text-white');
    });
    // Highlight active button
    const activeBtn = document.getElementById(`btn-${tabId}`);
    activeBtn.classList.remove('text-slate-400', 'hover:bg-slate-800/40', 'hover:text-white');
    activeBtn.classList.add('bg-blue-600', 'text-white', 'shadow-lg', 'shadow-blue-500/10');

    // Update Header
    const titles = {
        dashboard: { t: "Dashboard Overview", d: "Real-time flood intelligence and predictive risk telemetry" },
        predictor: { t: "🔮 Flood Severity Predictor", d: "Test what-if precipitation and antecedent soil scenarios on AI models" },
        wards: { t: "🏢 Ward Risk Profiler", d: "Gaussian Mixture Model (GMM) ward clustering and vulnerability profiles" },
        insights: { t: "📈 Data Insights & EDA", d: "Interactive visual exploratory analysis of monsoon historical dataset" },
        news: { t: "📰 News & Media NLP Analysis", d: "Independent news scraping validation feed and timeline index" },
        economic: { t: "💰 Economic Loss Simulator", d: "Simulate productivity loss and transit delays across severity categories" }
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
        btnM.className = "p-4 rounded-xl border border-blue-500 bg-blue-500/10 text-white font-bold transition-all duration-200";
        btnK.className = "p-4 rounded-xl border border-borderBg bg-slate-800/20 text-slate-400 hover:text-white transition-all duration-200";
    } else {
        btnK.className = "p-4 rounded-xl border border-blue-500 bg-blue-500/10 text-white font-bold transition-all duration-200";
        btnM.className = "p-4 rounded-xl border border-borderBg bg-slate-800/20 text-slate-400 hover:text-white transition-all duration-200";
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
    resDiv.innerHTML = `<div class="text-slate-300 animate-pulse">Executing ML Model Inference API...</div>`;

    try {
        const response = await fetch(`${API_BASE}/api/predict`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(reqData)
        });
        const data = await response.json();

        let bannerColor = "bg-emerald-500/10 border-emerald-500 text-emerald-400";
        let icon = "🟢";
        if (data.category === "Slight") {
            bannerColor = "bg-amber-500/10 border-amber-500 text-amber-400";
            icon = "🟡";
        } else if (data.category === "Moderate") {
            bannerColor = "bg-orange-500/10 border-orange-500 text-orange-400";
            icon = "🟠";
        } else if (data.category === "Severe") {
            bannerColor = "bg-red-500/10 border-red-500 text-red-400";
            icon = "🚨";
        }

        const probPct = (data.probability * 100).toFixed(1);

        resDiv.innerHTML = `
            <h3 class="font-bold text-lg">Inference Results (${data.scope === 'mumbai' ? 'Mumbai Model' : 'Konkan Stacking Model'})</h3>
            <div class="p-6 rounded-xl border ${bannerColor} flex flex-col gap-2">
                <h4 class="font-extrabold text-xl">${icon} ${data.category.toUpperCase().replace('_', ' ')} LIMIT</h4>
                <p class="text-sm text-slate-300 font-medium">${data.description}</p>
            </div>
            <div class="space-y-2">
                <div class="flex justify-between text-sm font-semibold">
                    <span>Flood Event Probability Score</span>
                    <span class="text-blue-400">${probPct}%</span>
                </div>
                <div class="w-full bg-slate-800 h-3 rounded-full overflow-hidden">
                    <div class="h-full transition-all duration-500" style="width: ${probPct}%; background-color: ${data.category === 'Severe' ? '#ef4444' : data.category === 'Moderate' ? '#f97316' : data.category === 'Slight' ? '#eab308' : '#10b981'}"></div>
                </div>
            </div>
        `;
    } catch (e) {
        resDiv.innerHTML = `<div class="text-red-400 font-medium">Failed to execute prediction: ${e.message}</div>`;
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

            let color = 'bg-blue-500';
            if (risk_level === 'High') color = 'bg-red-500';
            if (risk_level === 'Medium') color = 'bg-amber-500';

            container.innerHTML += `
                <div class="p-5 rounded-xl bg-slate-800/30 glass border-l-4 border-${risk_level === 'High' ? 'red-500' : risk_level === 'Medium' ? 'amber-500' : 'blue-500'} flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-center mb-2">
                            <span class="font-bold text-slate-200">Ward ${ward_code}</span>
                            <span class="text-xs font-semibold px-2.5 py-1 rounded-full ${risk_level === 'High' ? 'bg-red-500/10 text-red-400' : risk_level === 'Medium' ? 'bg-amber-500/10 text-amber-400' : 'bg-blue-500/10 text-blue-400'}">${risk_level.toUpperCase()} RISK</span>
                        </div>
                        <h4 class="text-xs text-slate-400 font-semibold mb-3 uppercase tracking-wider">${area_covered}</h4>
                        <div class="text-sm space-y-1.5 text-slate-300">
                            <div class="flex justify-between"><span>Known Flood Spots:</span> <span class="font-bold text-slate-100">${known_spots}</span></div>
                            <div class="flex justify-between"><span>Population at Risk:</span> <span class="font-bold text-slate-100">${pop_pct}%</span></div>
                            <div class="flex justify-between"><span>GMM Cluster Group:</span> <span class="font-bold text-slate-100">${cluster_label}</span></div>
                        </div>
                    </div>
                </div>
            `;
        });
    } catch (e) {
        container.innerHTML = `<div class="text-red-400 font-medium">Failed to load ward vulnerability details: ${e.message}</div>`;
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
                colorscale: 'OrRd',
                line: { width: 1, color: 'DarkSlateGrey' }
            },
            line: { color: 'rgba(255,255,255,0.1)' }
        };

        const layout = {
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
            font: { color: '#f1f5f9' },
            xaxis: { gridcolor: 'rgba(255,255,255,0.05)', linecolor: 'rgba(255,255,255,0.1)' },
            yaxis: { gridcolor: 'rgba(255,255,255,0.05)', linecolor: 'rgba(255,255,255,0.1)', range: [0, 16] },
            margin: { t: 20, b: 40, l: 40, r: 20 }
        };

        Plotly.newPlot('chart-timeline', [trace], layout, { responsive: true, displayModeBar: false });

        // 2. Render Cards
        grid.innerHTML = '';
        normalizedData.forEach(n => {
            let badgeColor = "bg-blue-500/10 text-blue-400 border border-blue-500/20";
            let border = "border-l-blue-500";
            if (n.severity_score >= 10) {
                badgeColor = "bg-red-500/10 text-red-400 border border-red-500/20";
                border = "border-l-red-500";
            } else if (n.severity_score >= 5) {
                badgeColor = "bg-amber-500/10 text-amber-400 border border-amber-500/20";
                border = "border-l-amber-500";
            }

            const keyBadges = n.keywords_found.split(',')
                .map(k => k.trim())
                .filter(k => k)
                .map(k => `<span class="bg-slate-800/50 text-slate-400 text-[10px] font-semibold px-2 py-0.5 rounded-md border border-borderBg">${k}</span>`)
                .join(' ');

            grid.innerHTML += `
                <div class="p-5 rounded-xl bg-slate-800/30 glass border-l-4 ${border} flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-center mb-3">
                            <span class="text-xs text-slate-400 font-bold">📅 ${n.related_date}</span>
                            <span class="text-xs font-bold px-2 py-0.5 rounded ${badgeColor}">Score: ${n.severity_score}</span>
                        </div>
                        <p class="text-sm font-medium italic text-slate-200 leading-relaxed mb-4">"${n.snippet_preview}"</p>
                    </div>
                    <div class="border-t border-borderBg/50 pt-3">
                        <div class="text-[10px] font-bold text-slate-500 uppercase tracking-wider mb-1.5">Extracted Tags</div>
                        <div class="flex flex-wrap gap-1">${keyBadges}</div>
                    </div>
                </div>
            `;
        });

    } catch (e) {
        grid.innerHTML = `<div class="text-red-400 font-medium">Failed to load media NLP news timeline feed: ${e.message}</div>`;
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
            marker: { color: m === 'July' ? '#ef4444' : '#3b82f6' }
        }));

        Plotly.newPlot('chart-month', boxTraces, {
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
            font: { color: '#f1f5f9' },
            xaxis: { gridcolor: 'rgba(255,255,255,0.05)', linecolor: 'rgba(255,255,255,0.1)' },
            yaxis: { gridcolor: 'rgba(255,255,255,0.05)', linecolor: 'rgba(255,255,255,0.1)', title: 'Rainfall (mm)' },
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
            marker: { color: '#3b82f6', size: 6, opacity: 0.6 }
        };

        const traceFlood = {
            x: floodDays.map(d => d.rainfall_mm),
            y: floodDays.map(d => d.rainfall_7day),
            mode: 'markers',
            name: 'Verified Flood Event',
            type: 'scatter',
            marker: { color: '#ef4444', size: 10, line: { width: 1, color: '#fff' } }
        };

        Plotly.newPlot('chart-scatter', [traceNormal, traceFlood], {
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
            font: { color: '#f1f5f9' },
            xaxis: { gridcolor: 'rgba(255,255,255,0.05)', linecolor: 'rgba(255,255,255,0.1)', title: 'Precipitation Intensity Today (mm)' },
            yaxis: { gridcolor: 'rgba(255,255,255,0.05)', linecolor: 'rgba(255,255,255,0.1)', title: '7-Day Soil Saturation (mm)' },
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
            colorscale: 'RdBu',
            zmin: -1, zmax: 1
        };

        Plotly.newPlot('chart-corr', [traceHeat], {
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)',
            font: { color: '#f1f5f9' },
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
