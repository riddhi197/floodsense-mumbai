// Detect environment and set API Base URL
const API_BASE = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' || window.location.protocol === 'file:' 
    ? 'http://127.0.0.1:8000' 
    : '';

let currentScope = 'mumbai';
let map = null;
let markersGroup = null;
let hazardBuffersGroup = null;

// Municipal Palette Tokens
const COLOR_HIGH = "#C9473D";   // Municipal Crimson
const COLOR_MED = "#D99A2B";    // Muted Amber
const COLOR_LOW = "#5F8A6A";    // Sage Green
const COLOR_ACCENT = "#D97745"; // Muted Hazard Orange

// AWS Weather Stations Coordinates & Multipliers (Fix C)
const AWS_STATIONS = {
    "santacruz": { name: "Santacruz AWS", lat: 19.0830, lon: 72.8530, rainOffset: 0, rain3dOffset: 0, rain7dOffset: 0 },
    "colaba": { name: "Colaba AWS", lat: 18.9150, lon: 72.8250, rainOffset: 15.0, rain3dOffset: 20.0, rain7dOffset: 35.0 },
    "rammandir": { name: "Ram Mandir AWS", lat: 19.1520, lon: 72.8420, rainOffset: 25.0, rain3dOffset: 30.0, rain7dOffset: 40.0 },
    "kurla": { name: "Kurla Mithi AWS", lat: 19.0650, lon: 72.8790, rainOffset: 30.0, rain3dOffset: 45.0, rain7dOffset: 60.0 }
};

// Ward Demographics & Risk Details Metadata
const WARD_METADATA = {
    "F/N": { name: "Ward F/N (Dadar East/Sion/Hindmata)", sqkm: 14.2, households: "215,400", population: "780,500", highRisk: "8.5 sq.km", medRisk: "3.2 sq.km", lowRisk: "2.5 sq.km", builtHt: "1.25m", subwayHt: "1.85m", roadHt: "1.10m", risk: "High" },
    "H/E": { name: "Ward H/E (Santacruz E/BKC/Milan Subway)", sqkm: 19.8, households: "290,100", population: "920,300", highRisk: "12.1 sq.km", medRisk: "4.5 sq.km", lowRisk: "3.2 sq.km", builtHt: "1.40m", subwayHt: "2.10m", roadHt: "1.25m", risk: "High" },
    "K/W": { name: "Ward K/W (Andheri West/Andheri Subway)", sqkm: 24.5, households: "340,800", population: "1,150,000", highRisk: "14.0 sq.km", medRisk: "6.2 sq.km", lowRisk: "4.3 sq.km", builtHt: "1.15m", subwayHt: "1.95m", roadHt: "0.95m", risk: "High" },
    "L": { name: "Ward L (Kurla/Mithi River Basin)", sqkm: 21.0, households: "310,500", population: "1,040,000", highRisk: "11.5 sq.km", medRisk: "5.5 sq.km", lowRisk: "4.0 sq.km", builtHt: "1.30m", subwayHt: "1.75m", roadHt: "1.05m", risk: "High" },
    "A": { name: "Ward A (Colaba/Churchgate/Marine Drive)", sqkm: 12.5, households: "110,200", population: "350,000", highRisk: "1.2 sq.km", medRisk: "2.8 sq.km", lowRisk: "8.5 sq.km", builtHt: "0.35m", subwayHt: "0.45m", roadHt: "0.25m", risk: "Low" },
    "G/S": { name: "Ward G/S (Worli/Lower Parel)", sqkm: 15.6, households: "180,400", population: "580,200", highRisk: "3.5 sq.km", medRisk: "6.1 sq.km", lowRisk: "6.0 sq.km", builtHt: "0.65m", subwayHt: "0.95m", roadHt: "0.55m", risk: "Medium" },
    "M/E": { name: "Ward M/E (Chembur East/Govandi)", sqkm: 32.4, households: "285,600", population: "910,400", highRisk: "15.2 sq.km", medRisk: "9.1 sq.km", lowRisk: "8.1 sq.km", builtHt: "1.10m", subwayHt: "1.50m", roadHt: "0.90m", risk: "High" },
    "P/S": { name: "Ward P/S (Goregaon/Charkop)", sqkm: 28.2, households: "260,300", population: "840,100", highRisk: "6.2 sq.km", medRisk: "11.0 sq.km", lowRisk: "11.0 sq.km", builtHt: "0.75m", subwayHt: "1.15m", roadHt: "0.65m", risk: "Medium" }
};

// Ward GIS Map Locations (Coordinates)
const WARD_MAP_POINTS = [
    { code: "F/N", lat: 19.0370, lon: 72.8620, zone: "island", risk: "High", title: "Ward F/N - Sion / Hindmata (Chronic Flooding)" },
    { code: "H/E", lat: 19.0830, lon: 72.8530, zone: "western", risk: "High", title: "Ward H/E - Milan Subway & BKC Node" },
    { code: "K/W", lat: 19.1190, lon: 72.8470, zone: "western", risk: "High", title: "Ward K/W - Andheri Subway" },
    { code: "L", lat: 19.0650, lon: 72.8790, zone: "eastern", risk: "High", title: "Ward L - Kurla Mithi River Basin" },
    { code: "A", lat: 18.9150, lon: 72.8250, zone: "island", risk: "Low", title: "Ward A - Colaba & Marine Drive" },
    { code: "G/S", lat: 18.9980, lon: 72.8150, zone: "island", risk: "Medium", title: "Ward G/S - Worli & Sea Link" },
    { code: "M/E", lat: 19.0510, lon: 72.9120, zone: "eastern", risk: "High", title: "Ward M/E - Chembur & Govandi" },
    { code: "P/S", lat: 19.1620, lon: 72.8450, zone: "western", risk: "Medium", title: "Ward P/S - Goregaon" }
];

// Fallback Embedded Datasets for offline / standalone file browsing
const FALLBACK_WARDS = [
    {"Ward_Code": "F/N", "Area_Covered": "Dadar East / Sion / Hindmata", "Risk_Level": "High", "Known_Flood_Spots_Count": 12, "Population_At_Risk_Pct": 60.0, "Cluster_Label": "High Risk Tier 1"},
    {"Ward_Code": "H/E", "Area_Covered": "Santacruz East / BKC / Milan Subway", "Risk_Level": "High", "Known_Flood_Spots_Count": 14, "Population_At_Risk_Pct": 65.0, "Cluster_Label": "High Risk Tier 1"},
    {"Ward_Code": "K/W", "Area_Covered": "Andheri West / Andheri Subway", "Risk_Level": "High", "Known_Flood_Spots_Count": 11, "Population_At_Risk_Pct": 55.0, "Cluster_Label": "High Risk Tier 1"},
    {"Ward_Code": "L", "Area_Covered": "Kurla / Mithi River Basin", "Risk_Level": "High", "Known_Flood_Spots_Count": 8, "Population_At_Risk_Pct": 48.0, "Cluster_Label": "High Risk Tier 1"},
    {"Ward_Code": "M/E", "Area_Covered": "Chembur East / Govandi", "Risk_Level": "High", "Known_Flood_Spots_Count": 10, "Population_At_Risk_Pct": 52.0, "Cluster_Label": "High Risk Tier 1"},
    {"Ward_Code": "G/N", "Area_Covered": "Dadar West / Matunga", "Risk_Level": "Medium", "Known_Flood_Spots_Count": 7, "Population_At_Risk_Pct": 45.0, "Cluster_Label": "Medium Risk Tier 2"},
    {"Ward_Code": "G/S", "Area_Covered": "Worli / Lower Parel", "Risk_Level": "Medium", "Known_Flood_Spots_Count": 5, "Population_At_Risk_Pct": 35.0, "Cluster_Label": "Medium Risk Tier 2"},
    {"Ward_Code": "P/S", "Area_Covered": "Goregaon / Charkop", "Risk_Level": "Medium", "Known_Flood_Spots_Count": 5, "Population_At_Risk_Pct": 38.0, "Cluster_Label": "Medium Risk Tier 2"},
    {"Ward_Code": "A", "Area_Covered": "Colaba / Churchgate / Marine Drive", "Risk_Level": "Low", "Known_Flood_Spots_Count": 2, "Population_At_Risk_Pct": 15.0, "Cluster_Label": "Safe Tier 3"},
    {"Ward_Code": "D", "Area_Covered": "Malabar Hill / Grant Road", "Risk_Level": "Low", "Known_Flood_Spots_Count": 3, "Population_At_Risk_Pct": 12.0, "Cluster_Label": "Safe Tier 3"}
];

const FALLBACK_NEWS = [
    {"Snippet_ID": 7, "Related_Date": "2021-07-18", "Severity_Score": 15, "Keywords_Found": "death, deaths, landslide, landslides, severe, flooding, heavy", "Snippet_Preview": "Heavy rainfall on 18 July 2021 caused landslides and flooding that resulted in over 20 deaths in Mumbai."},
    {"Snippet_ID": 8, "Related_Date": "2021-07-22", "Severity_Score": 9, "Keywords_Found": "landslide, landslides, evacuation, flooding, heavy", "Snippet_Preview": "Starting on 22 July 2021, Maharashtra saw heavy rainfall across many western districts, with widespread inundation."},
    {"Snippet_ID": 9, "Related_Date": "2023-07-20", "Severity_Score": 8, "Keywords_Found": "landslide, severe, disruption, flooding, heavy", "Snippet_Preview": "On 20 July 2023, heavy rain triggered a landslide and severe flooding conditions, primarily affecting transport."},
    {"Snippet_ID": 5, "Related_Date": "2021-06-09", "Severity_Score": 8, "Keywords_Found": "fatalities, collapse, waterlogging, heavy", "Snippet_Preview": "The Southwest Monsoon arrived in Mumbai with dramatic effect on 9 June 2021, bringing heavy downpours and waterlogging."},
    {"Snippet_ID": 3, "Related_Date": "2019-07-02", "Severity_Score": 7, "Keywords_Found": "severe, extreme, disrupted, flooding, waterlogging", "Snippet_Preview": "On 2nd July 2019, Mumbai recorded extreme rainfall of 200.12 mm in a single day, leading to severe suburban train disruption."},
    {"Snippet_ID": 4, "Related_Date": "2020-09-24", "Severity_Score": 7, "Keywords_Found": "died, extreme, inundated, heavy", "Snippet_Preview": "Local media reported that 2 people died in a flooded building in Agripada, Mumbai on 24 September 2020."},
    {"Snippet_ID": 6, "Related_Date": "2021-07-16", "Severity_Score": 4, "Keywords_Found": "extreme, flooding, waterlogging", "Snippet_Preview": "An extreme rainfall day of 199.87 mm was recorded on 16th July 2021, contributing to significant localized flooding."},
    {"Snippet_ID": 2, "Related_Date": "2018-06-25", "Severity_Score": 4, "Keywords_Found": "extreme, disruption, waterlogging", "Snippet_Preview": "An extreme rainfall event of 153.14 mm occurred on 25th June 2018, causing significant waterlogging in low-lying areas."},
    {"Snippet_ID": 10, "Related_Date": "2022-08-10", "Severity_Score": 4, "Keywords_Found": "severe, flooding, waterlogging", "Snippet_Preview": "Severe waterlogging has repeatedly been reported from chronic flooding spots including Dadar, Sion, and Kurla."},
    {"Snippet_ID": 1, "Related_Date": "2018-06-24", "Severity_Score": 3, "Keywords_Found": "severe, waterlogging", "Snippet_Preview": "On 24 June 2018, Mumbai received over 150 mm of rainfall over a 24 hour period, causing street inundation."},
    {"Snippet_ID": 11, "Related_Date": "2023-08-01", "Severity_Score": 3, "Keywords_Found": "flooding, waterlogging, heavy", "Snippet_Preview": "BMC identified 221 spots citywide prone to waterlogging and flooding, with wards H-East, K-West, and F-North at top risk."},
    {"Snippet_ID": 12, "Related_Date": "2023-09-15", "Severity_Score": 1, "Keywords_Found": "flooding", "Snippet_Preview": "BMC data indicates that 35 percent of Mumbai's population is at flood risk overall."}
];

const FALLBACK_HISTORICAL = [
    { Month: 6, Rainfall_mm: 45.0, Rainfall_3day: 80.0, Rainfall_7day: 150.0, Confirmed_Event: 0 },
    { Month: 6, Rainfall_mm: 120.0, Rainfall_3day: 190.0, Rainfall_7day: 310.0, Confirmed_Event: 0 },
    { Month: 7, Rainfall_mm: 230.0, Rainfall_3day: 420.0, Rainfall_7day: 680.0, Confirmed_Event: 1 },
    { Month: 7, Rainfall_mm: 180.0, Rainfall_3day: 350.0, Rainfall_7day: 520.0, Confirmed_Event: 1 },
    { Month: 7, Rainfall_mm: 60.0, Rainfall_3day: 110.0, Rainfall_7day: 240.0, Confirmed_Event: 0 },
    { Month: 8, Rainfall_mm: 210.0, Rainfall_3day: 390.0, Rainfall_7day: 610.0, Confirmed_Event: 1 },
    { Month: 8, Rainfall_mm: 85.0, Rainfall_3day: 140.0, Rainfall_7day: 280.0, Confirmed_Event: 0 },
    { Month: 9, Rainfall_mm: 190.0, Rainfall_3day: 330.0, Rainfall_7day: 550.0, Confirmed_Event: 1 },
    { Month: 9, Rainfall_mm: 40.0, Rainfall_3day: 75.0, Rainfall_7day: 160.0, Confirmed_Event: 0 },
    { Month: 10, Rainfall_mm: 15.0, Rainfall_3day: 30.0, Rainfall_7day: 70.0, Confirmed_Event: 0 }
];

// INITIALIZE LEAFLET GIS MAP WITH FLOOD INUNDATION HAZARD OVERLAY & LEGEND
function initGisMap() {
    const mapDiv = document.getElementById('leaflet-map');
    if (mapDiv && !map) {
        try {
            map = L.map('leaflet-map').setView([19.0760, 72.8777], 11);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 18,
                attribution: '© OpenStreetMap contributors, Esri GIS'
            }).addTo(map);

            hazardBuffersGroup = L.layerGroup().addTo(map);
            markersGroup = L.layerGroup().addTo(map);

            // Add Flood Inundation Risk Buffer Rings around Chronic Hotspots
            addFloodHazardOverlay();

            // Render Ward Markers
            renderWardMarkers('all');

            // Add Municipal Map Legend
            addMapLegend();
        } catch (e) {
            console.warn("Leaflet Map init error: ", e);
        }
    }
}

// ADD FLOOD INUNDATION BUFFER RINGS (Sion, Kurla Mithi River, Milan Subway, Andheri Subway)
function addFloodHazardOverlay() {
    if (!hazardBuffersGroup) return;
    hazardBuffersGroup.clearLayers();

    const floodZones = [
        { lat: 19.0370, lon: 72.8620, radius: 1800, color: COLOR_HIGH, label: "Ward F/N - Sion Inundation Basin" },
        { lat: 19.0830, lon: 72.8530, radius: 1500, color: COLOR_HIGH, label: "Ward H/E - Milan Subway Basin" },
        { lat: 19.0650, lon: 72.8790, radius: 2200, color: COLOR_HIGH, label: "Ward L - Mithi River Floodplain" },
        { lat: 19.1190, lon: 72.8470, radius: 1400, color: COLOR_HIGH, label: "Ward K/W - Andheri Inundation Zone" }
    ];

    floodZones.forEach(fz => {
        const buffer = L.circle([fz.lat, fz.lon], {
            radius: fz.radius,
            color: fz.color,
            weight: 1.5,
            fillColor: fz.color,
            fillOpacity: 0.18,
            dashArray: '4, 4'
        });
        buffer.bindTooltip(`<b>🌊 ${fz.label}</b><br/>100-Year Peak Flood Risk Radius`, { sticky: true });
        hazardBuffersGroup.addLayer(buffer);
    });
}

// ADD MUNICIPAL GIS LEGEND TO LEAFLET MAP
function addMapLegend() {
    if (!map) return;
    const legend = L.control({ position: 'bottomright' });

    legend.onAdd = function () {
        const div = L.DomUtil.create('div', 'info legend');
        div.style.backgroundColor = '#ffffff';
        div.style.padding = '8px 12px';
        div.style.borderRadius = '6px';
        div.style.border = '1px solid #E2DFD7';
        div.style.fontFamily = 'Space Grotesk, monospace';
        div.style.fontSize = '10px';
        div.style.color = '#252525';
        div.style.boxShadow = '0 2px 4px rgba(0,0,0,0.08)';

        div.innerHTML = `
            <div style="font-weight: 800; border-bottom: 1px solid #E2DFD7; padding-bottom: 4px; margin-bottom: 6px; text-transform: uppercase;">
                🌊 Flood Risk Inundation Legend
            </div>
            <div style="display: flex; items-center; gap: 6px; margin-bottom: 3px;">
                <span style="width: 10px; height: 10px; border-radius: 50%; background: ${COLOR_HIGH}; display: inline-block;"></span>
                <b>Chronic Flood Spot (Very High)</b>
            </div>
            <div style="display: flex; items-center; gap: 6px; margin-bottom: 3px;">
                <span style="width: 10px; height: 10px; border-radius: 50%; background: ${COLOR_MED}; display: inline-block;"></span>
                <b>Subway / Waterlogging Node (Moderate)</b>
            </div>
            <div style="display: flex; items-center; gap: 6px; margin-bottom: 3px;">
                <span style="width: 10px; height: 10px; border-radius: 50%; background: ${COLOR_LOW}; display: inline-block;"></span>
                <b>Coastline / High Ground (Low Risk)</b>
            </div>
            <div style="display: flex; items-center; gap: 6px; margin-top: 4px; border-top: 1px border #E2DFD7; pt: 3px;">
                <span style="width: 12px; height: 8px; border-radius: 2px; background: rgba(201, 71, 61, 0.25); border: 1px dashed ${COLOR_HIGH}; display: inline-block;"></span>
                <span>100-Year Flood Inundation Buffer Zone</span>
            </div>
        `;
        return div;
    };

    legend.addTo(map);
}

// RENDER GIS MAP MARKERS
function renderWardMarkers(filterZoneStr = 'all') {
    if (!markersGroup) return;
    markersGroup.clearLayers();

    WARD_MAP_POINTS.forEach(pt => {
        if (filterZoneStr !== 'all' && pt.zone !== filterZoneStr) return;

        let color = COLOR_LOW;
        if (pt.risk === "High") color = COLOR_HIGH;
        if (pt.risk === "Medium") color = COLOR_MED;

        const circle = L.circleMarker([pt.lat, pt.lon], {
            radius: 9,
            fillColor: color,
            color: "#ffffff",
            weight: 2,
            opacity: 1,
            fillOpacity: 0.85
        });

        circle.bindPopup(`
            <div style="font-family: Outfit, sans-serif; padding: 4px;">
                <b style="color: #252525; font-size: 13px;">${pt.title}</b><br/>
                <span style="font-size: 11px; color: ${color}; font-weight: 800;">Risk Category: ${pt.risk.toUpperCase()}</span><br/>
                <button onclick="selectWard('${pt.code}')" style="margin-top: 6px; background: ${COLOR_ACCENT}; color: white; border: none; padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; cursor: pointer;">
                    View Ward Inundation Height & Demographics
                </button>
            </div>
        `);

        circle.on('click', () => {
            selectWard(pt.code);
        });

        markersGroup.addLayer(circle);
    });
}

// FILTER BY REGION / ZONE
function filterZone(zoneStr) {
    document.querySelectorAll('.filter-btn').forEach(btn => {
        if (btn.id && btn.id.startsWith('zone-')) {
            btn.classList.remove('active');
        }
    });

    const activeBtn = document.getElementById(`zone-${zoneStr}`);
    if (activeBtn) activeBtn.classList.add('active');

    renderWardMarkers(zoneStr);
}

// SELECT SPECIFIC WARD (UPDATE HEIGHT DIAGRAM & DEMOGRAPHICS)
function selectWard(wardCode) {
    const meta = WARD_METADATA[wardCode];
    if (!meta) return;

    // Update Titles
    const titleEl = document.getElementById('selected-ward-title');
    if (titleEl) titleEl.innerText = `Ward ${wardCode}`;

    const infoLabel = document.getElementById('info-ward-label');
    if (infoLabel) infoLabel.innerText = meta.name.toUpperCase();

    // Update Demographics Cards
    const sqkmEl = document.getElementById('info-sqkm');
    if (sqkmEl) sqkmEl.innerText = meta.sqkm;

    const houseEl = document.getElementById('info-households');
    if (houseEl) houseEl.innerText = meta.households;

    const popEl = document.getElementById('info-population');
    if (popEl) popEl.innerText = meta.population;

    const highEl = document.getElementById('info-high-risk');
    if (highEl) highEl.innerText = meta.highRisk;

    const medEl = document.getElementById('info-med-risk');
    if (medEl) medEl.innerText = meta.medRisk;

    const lowEl = document.getElementById('info-low-risk');
    if (lowEl) lowEl.innerText = meta.lowRisk;

    // Update Architectural Flood Height Bar Chart
    const txtBuilt = document.getElementById('txt-built');
    if (txtBuilt) txtBuilt.innerText = meta.builtHt;

    const txtSubway = document.getElementById('txt-subway');
    if (txtSubway) txtSubway.innerText = meta.subwayHt;

    const txtRoads = document.getElementById('txt-roads');
    if (txtRoads) txtRoads.innerText = meta.roadHt;

    const bBuilt = document.getElementById('bar-built');
    if (bBuilt) bBuilt.style.height = `${(parseFloat(meta.builtHt) / 2.5) * 100}%`;

    const bSubway = document.getElementById('bar-subway');
    if (bSubway) bSubway.style.height = `${(parseFloat(meta.subwayHt) / 2.5) * 100}%`;

    const bRoads = document.getElementById('bar-roads');
    if (bRoads) bRoads.style.height = `${(parseFloat(meta.roadHt) / 2.5) * 100}%`;

    // Center map on ward if point exists
    const pt = WARD_MAP_POINTS.find(p => p.code === wardCode);
    if (pt && map) {
        map.setView([pt.lat, pt.lon], 13);
    }
}

// Left Sidebar Tab Switching
function switchTab(tabId) {
    document.querySelectorAll('main > section').forEach(section => {
        section.classList.add('hidden');
    });
    const targetSection = document.getElementById(`tab-${tabId}`);
    if (targetSection) targetSection.classList.remove('hidden');

    document.querySelectorAll('.sidebar-btn').forEach(btn => {
        btn.classList.remove('active');
        const iconEl = btn.querySelector('i');
        if (iconEl) iconEl.className = "w-5 h-5 mt-0.5 text-slate-600 flex-shrink-0";
    });

    const activeBtn = document.getElementById(`btn-${tabId}`);
    if (activeBtn) {
        activeBtn.classList.add('active');
        const iconEl = activeBtn.querySelector('i');
        if (iconEl) iconEl.className = "w-5 h-5 mt-0.5 text-[#D97745] flex-shrink-0";
    }

    if (tabId === 'map' && map) {
        setTimeout(() => { map.invalidateSize(); }, 200);
    }

    if (tabId === 'wards') loadWards();
    if (tabId === 'news') loadNews();
    if (tabId === 'insights') loadInsights();
    if (tabId === 'logistics') runEconomicSim();
}

// FIX C: CHANGE AUTOMATIC WEATHER STATION (AWS) TELEMETRY
function changeAwsStation() {
    const awsKey = document.getElementById('select-aws').value;
    const st = AWS_STATIONS[awsKey] || AWS_STATIONS['santacruz'];

    const baseRain = 85.0;
    const base3d = 120.0;
    const base7d = 250.0;

    document.getElementById('input-rain').value = (baseRain + st.rainOffset).toFixed(1);
    document.getElementById('input-rain3d').value = (base3d + st.rain3dOffset).toFixed(1);
    document.getElementById('input-rain7d').value = (base7d + st.rain7dOffset).toFixed(1);

    syncInput('rain');
    syncInput('rain3d');
    syncInput('rain7d');

    if (map && st.lat && st.lon) {
        map.setView([st.lat, st.lon], 12);
    }

    runInference();
}

// Stepper Button Handler (+ / - buttons)
function stepVal(type, delta) {
    const inputEl = document.getElementById(`input-${type}`);
    if (!inputEl) return;
    let currVal = parseFloat(inputEl.value) || 0;
    currVal += delta;
    if (type === 'month') {
        currVal = Math.max(6, Math.min(10, currVal));
    } else if (type === 'tide') {
        currVal = Math.max(0.5, Math.min(5.5, currVal));
    } else {
        currVal = Math.max(0, currVal);
    }
    inputEl.value = currVal;
    syncInput(type);
}

// Update stepper display text
function syncInput(type) {
    const val = parseFloat(document.getElementById(`input-${type}`).value) || 0;
    const txtEl = document.getElementById(`val-${type}`);
    if (!txtEl) return;

    if (type === 'rain') txtEl.innerText = `${val.toFixed(1)} mm`;
    if (type === 'rain3d') txtEl.innerText = `${val.toFixed(1)} mm`;
    if (type === 'rain7d') txtEl.innerText = `${val.toFixed(1)} mm`;
    if (type === 'tide') txtEl.innerText = `${val.toFixed(2)} m`;
    if (type === 'month') {
        const months = {6: 'June (6)', 7: 'July (7)', 8: 'August (8)', 9: 'September (9)', 10: 'October (10)'};
        txtEl.innerText = months[val] || `Month (${val})`;
    }
}

// Set model scope
function setScope(scope) {
    currentScope = scope;
    const btnM = document.getElementById('scope-mumbai');
    const btnK = document.getElementById('scope-konkan');

    if (scope === 'mumbai') {
        btnM.className = "p-2.5 rounded border border-[#D97745] bg-[#F5F3EE] text-[#252525] font-bold transition-all font-mono";
        btnK.className = "p-2.5 rounded border border-[#E2DFD7] bg-white text-slate-600 hover:text-[#252525] transition-all font-mono";
    } else {
        btnK.className = "p-2.5 rounded border border-[#D97745] bg-[#F5F3EE] text-[#252525] font-bold transition-all font-mono";
        btnM.className = "p-2.5 rounded border border-[#E2DFD7] bg-white text-slate-600 hover:text-[#252525] transition-all font-mono";
    }
}

// FETCH REAL-TIME LIVE WEATHER FROM OPEN-METEO API FOR MUMBAI
async function fetchLiveWeather() {
    const statusBadges = document.querySelectorAll('#live-badge');
    statusBadges.forEach(el => {
        if (el) el.innerText = "Syncing Open-Meteo...";
    });

    try {
        const url = "https://api.open-meteo.com/v1/forecast?latitude=18.96&longitude=72.82&hourly=precipitation&past_days=7&forecast_days=1&timezone=Asia%2FKolkata";
        const res = await fetch(url);
        const data = await res.json();

        if (data && data.hourly && data.hourly.precipitation) {
            const precipList = data.hourly.precipitation;
            const totalHours = precipList.length;

            // Today's rain (last 24h)
            const todayRainList = precipList.slice(totalHours - 24);
            const rainToday = todayRainList.reduce((a, b) => a + b, 0);

            // 3-Day antecedent (last 72h)
            const rain3d = precipList.slice(totalHours - 72).reduce((a, b) => a + b, 0);

            // 7-Day antecedent (last 168h)
            const rain7d = precipList.slice(0, 168).reduce((a, b) => a + b, 0);

            // Current Month
            const currentMonth = new Date().getMonth() + 1;
            const monthVal = (currentMonth >= 6 && currentMonth <= 10) ? currentMonth : 7;

            // Update Input Elements
            document.getElementById('input-rain').value = rainToday.toFixed(1);
            document.getElementById('input-rain3d').value = rain3d.toFixed(1);
            document.getElementById('input-rain7d').value = rain7d.toFixed(1);
            document.getElementById('input-month').value = monthVal;

            // Sync Stepper Label Texts
            syncInput('rain');
            syncInput('rain3d');
            syncInput('rain7d');
            syncInput('month');

            // Auto-trigger prediction inference & auto-sync logistics!
            await runInference();
        }
    } catch (e) {
        console.warn("Open-Meteo live weather fetch failed, using stored precipitation defaults: ", e);
    }
}

// RUN PREDICTION MODEL INFERENCE (FACTORING IN FIX A TIDE HEIGHT & FIX C AWS)
async function runInference() {
    const reqData = {
        scope: currentScope,
        rain_today: parseFloat(document.getElementById('input-rain').value) || 85.0,
        rain_3d: parseFloat(document.getElementById('input-rain3d').value) || 120.0,
        rain_7d: parseFloat(document.getElementById('input-rain7d').value) || 250.0,
        tide_height_m: parseFloat(document.getElementById('input-tide').value) || 3.4,
        month_val: parseInt(document.getElementById('input-month').value) || 7
    };

    const resDiv = document.getElementById('prediction-result');
    if (resDiv) {
        resDiv.classList.remove('hidden');
        resDiv.innerHTML = `<div class="text-[#D97745] font-bold font-mono animate-pulse flex items-center gap-2"><i data-lucide="cpu" class="w-4 h-4"></i> Executing Machine Learning Hydro Inference...</div>`;
    }

    let data;
    try {
        const response = await fetch(`${API_BASE}/api/predict`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(reqData)
        });
        if (response.ok) {
            data = await response.json();
        }
    } catch (e) {
        console.warn("Backend API unavailable, using local client JS model calculation.");
    }

    if (!data || !data.probability) {
        let prob = 0.05;
        // Factor in Tide Height Booster (Fix A)
        let tideBoost = 0.0;
        if (reqData.tide_height_m >= 4.2) {
            tideBoost = 0.25; // High Spring Tide compounding effect!
        } else if (reqData.tide_height_m >= 3.8) {
            tideBoost = 0.12;
        }

        if (reqData.scope === 'mumbai') {
            prob = Math.min(0.98, (reqData.rain_today * 0.004) + (reqData.rain_3d * 0.0018) + (reqData.rain_7d * 0.0008) + tideBoost);
        } else {
            prob = Math.min(0.98, (reqData.rain_today * 0.0045) + (reqData.rain_3d * 0.002) + (reqData.rain_7d * 0.001) + tideBoost);
        }
        let category = "No_Flood";
        let description = "All systems normal. Weather & tide conditions are within safe historical thresholds.";
        if (prob >= 0.85) {
            category = "Severe";
            description = "Emergency alert! Massive divisional flooding expected. Rivers approaching danger levels. Avoid travel.";
        } else if (prob >= 0.70) {
            category = "Moderate";
            description = "Significant waterlogging in key traffic subway nodes. Local train services may experience delays.";
        } else if (prob >= 0.50) {
            category = "Slight";
            description = "Waterlogging expected in chronic low-lying areas. Minor traffic slow-downs.";
        }
        data = { scope: reqData.scope, probability: prob, category: category, description: description };
    }

    // Auto-sync Logistics Severity Dropdown to AI Prediction Result!
    const ecoSelect = document.getElementById('eco-severity');
    if (ecoSelect) {
        ecoSelect.value = data.category;
        runEconomicSim(); // Trigger logistics calculation automatically!
    }

    let bannerColor = "bg-emerald-50 border-emerald-200 text-[#5F8A6A]";
    let icon = "🟢";
    if (data.category === "Slight") {
        bannerColor = "bg-amber-50 border-amber-200 text-[#D99A2B]";
        icon = "🟡";
    } else if (data.category === "Moderate") {
        bannerColor = "bg-orange-50 border-orange-200 text-[#D97745]";
        icon = "🟠";
    } else if (data.category === "Severe") {
        bannerColor = "bg-red-50 border-red-200 text-[#C9473D]";
        icon = "🚨";
    }

    const probPct = (data.probability * 100).toFixed(1);

    // FIX A: Check High Tide Alert Banner (>4.2m)
    let tideAlertBanner = '';
    if (reqData.tide_height_m >= 4.2) {
        tideAlertBanner = `
            <div class="p-3 bg-red-100 border border-red-300 rounded text-xs text-[#C9473D] font-mono font-extrabold flex items-center gap-2">
                <span>🚨 ASTRONOMICAL HIGH TIDE WARNING (${reqData.tide_height_m.toFixed(2)}m):</span>
                <span>BMC Sea Floodgates Closed (Love Grove & Britannia)! Inundation Back-Up Active!</span>
            </div>
        `;
    }

    if (resDiv) {
        resDiv.innerHTML = `
            <div class="flex justify-between items-center border-b border-[#E2DFD7] pb-3">
                <h3 class="font-bold text-base text-[#252525] flex items-center gap-2 font-mono">
                    <i data-lucide="shield-alert" class="w-5 h-5 text-[#D97745]"></i>
                    AI Hydro Model Result (${data.scope === 'mumbai' ? 'Mumbai City XGBoost' : 'Konkan Stacking Ensemble'})
                </h3>
                <span class="text-xs font-bold font-mono px-3 py-1 rounded-full ${bannerColor}">${probPct}% RISK SCORE</span>
            </div>
            ${tideAlertBanner}
            <div class="p-5 rounded border ${bannerColor} flex flex-col gap-2">
                <h4 class="font-extrabold text-lg">${icon} ${data.category.toUpperCase().replace('_', ' ')} CATEGORY</h4>
                <p class="text-sm text-slate-800 font-medium">${data.description}</p>
            </div>
            <div class="space-y-2">
                <div class="flex justify-between text-xs font-bold text-[#252525] font-mono">
                    <span>Flood Risk Probability Gauge</span>
                    <span class="text-[#D97745]">${probPct}%</span>
                </div>
                <div class="w-full bg-[#F5F3EE] h-3.5 rounded overflow-hidden border border-[#E2DFD7] p-0.5">
                    <div class="h-full rounded transition-all duration-700" style="width: ${probPct}%; background: ${data.category === 'Severe' ? 'linear-gradient(90deg, #D99A2B, #C9473D)' : data.category === 'Moderate' ? 'linear-gradient(90deg, #D97745, #D99A2B)' : 'linear-gradient(90deg, #5F8A6A, #D97745)'}"></div>
                </div>
            </div>
        `;
        lucide.createIcons();
    }
}

// FILTER MUNICIPAL WARD GRID CARDS
function filterWardGrid(riskCategory) {
    ['all', 'high', 'med', 'low'].forEach(k => {
        const btn = document.getElementById(`wgrid-${k}`);
        if (btn) {
            btn.className = "px-3 py-1.5 rounded border border-[#E2DFD7] bg-white text-[#252525] font-bold hover:bg-[#F5F3EE]";
        }
    });

    let activeKey = 'all';
    if (riskCategory === 'High') activeKey = 'high';
    if (riskCategory === 'Medium') activeKey = 'med';
    if (riskCategory === 'Low') activeKey = 'low';

    const activeBtn = document.getElementById(`wgrid-${activeKey}`);
    if (activeBtn) {
        if (riskCategory === 'High') activeBtn.className = "px-3 py-1.5 rounded border border-[#C9473D] bg-[#C9473D] text-white font-bold";
        else if (riskCategory === 'Medium') activeBtn.className = "px-3 py-1.5 rounded border border-[#D99A2B] bg-[#D99A2B] text-white font-bold";
        else if (riskCategory === 'Low') activeBtn.className = "px-3 py-1.5 rounded border border-[#5F8A6A] bg-[#5F8A6A] text-white font-bold";
        else activeBtn.className = "px-3 py-1.5 rounded border border-[#D97745] bg-[#D97745] text-white font-bold";
    }

    loadWards(riskCategory);
}

// FETCH & POPULATE MUNICIPAL WARD CARDS GRID
async function loadWards(filterRisk = 'all') {
    const container = document.getElementById('wards-container');
    if (!container) return;

    let data;
    try {
        const response = await fetch(`${API_BASE}/api/wards`);
        const json = await response.json();
        if (response.ok && Array.isArray(json)) {
            data = json;
        }
    } catch (e) {
        console.warn("Backend API unavailable, using local embedded ward dataset.");
    }
    if (!data || !Array.isArray(data)) {
        data = FALLBACK_WARDS;
    }

    container.innerHTML = '';
    data.forEach(w => {
        const risk_level = w.Risk_Level || w.risk_level || 'Low';
        if (filterRisk !== 'all' && risk_level !== filterRisk) return;

        const ward_code = w.Ward_Code || w.ward_code || '';
        const area_covered = w.Area_Covered || w.area_covered || '';
        const known_spots = w.Known_Flood_Spots_Count !== undefined ? w.Known_Flood_Spots_Count : w.known_flood_spots_count;
        const pop_pct = w.Population_At_Risk_Pct !== undefined ? w.Population_At_Risk_Pct : w.population_at_risk_pct;
        const cluster_label = w.Cluster_Label || w.cluster_label || '';

        let borderClass = 'border-l-[#5F8A6A]';
        let badgeClass = 'bg-emerald-50 text-[#5F8A6A] border-emerald-200';
        let riskIcon = '🟢';
        if (risk_level === 'High') {
            borderClass = 'border-l-[#C9473D]';
            badgeClass = 'bg-red-50 text-[#C9473D] border-red-200';
            riskIcon = '🔴';
        } else if (risk_level === 'Medium') {
            borderClass = 'border-l-[#D99A2B]';
            badgeClass = 'bg-amber-50 text-[#D99A2B] border-amber-200';
            riskIcon = '🟠';
        }

        container.innerHTML += `
            <div class="p-5 rounded-lg bg-white border border-[#E2DFD7] border-l-4 ${borderClass} flex flex-col justify-between space-y-4 shadow-sm hover:shadow-md transition-all">
                <div>
                    <div class="flex justify-between items-center mb-2">
                        <span class="font-extrabold text-[#252525] text-sm font-mono flex items-center gap-1.5">
                            <span>${riskIcon}</span> WARD ${ward_code}
                        </span>
                        <span class="text-[10px] font-extrabold font-mono px-2.5 py-0.5 rounded border ${badgeClass}">${risk_level.toUpperCase()} RISK</span>
                    </div>
                    <h4 class="text-xs text-slate-800 font-bold uppercase tracking-wider leading-snug">${area_covered}</h4>
                </div>
                <div class="text-xs space-y-2 text-slate-700 border-t border-[#E2DFD7] pt-3 font-mono">
                    <div class="flex justify-between"><span>Known Flood Spots:</span> <b class="text-[#252525]">${known_spots} Hotspots</b></div>
                    <div class="flex justify-between"><span>Population Exposure:</span> <b class="text-[#252525]">${pop_pct}% at Risk</b></div>
                    <div class="flex justify-between"><span>GMM Cluster Tier:</span> <b class="text-[#252525]">${cluster_label}</b></div>
                </div>
            </div>
        `;
    });
}

// Fetch NLP News timeline and cards
async function loadNews() {
    const grid = document.getElementById('news-grid');
    if (!grid) return;

    let data;
    try {
        const response = await fetch(`${API_BASE}/api/news`);
        const json = await response.json();
        if (response.ok && Array.isArray(json)) {
            data = json;
        }
    } catch (e) {
        console.warn("Backend API unavailable, using local embedded news dataset.");
    }
    if (!data || !Array.isArray(data)) {
        data = FALLBACK_NEWS;
    }

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
            line: { width: 1, color: '#D97745' }
        },
        line: { color: 'rgba(217, 119, 69, 0.4)' }
    };

    const layout = {
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: { color: '#252525' },
        xaxis: { gridcolor: 'rgba(0,0,0,0.06)', linecolor: 'rgba(0,0,0,0.1)' },
        yaxis: { gridcolor: 'rgba(0,0,0,0.06)', linecolor: 'rgba(0,0,0,0.1)', range: [0, 16], title: 'Severity Score' },
        margin: { t: 20, b: 40, l: 40, r: 20 }
    };

    Plotly.newPlot('chart-timeline', [trace], layout, { responsive: true, displayModeBar: false });

    // 2. Render Cards
    grid.innerHTML = '';
    normalizedData.forEach(n => {
        let badgeColor = "bg-[#F5F3EE] text-slate-700 border border-[#E2DFD7]";
        let border = "border-l-[#D97745]";
        if (n.severity_score >= 10) {
            badgeColor = "bg-red-50 text-[#C9473D] border border-red-200";
            border = "border-l-[#C9473D]";
        } else if (n.severity_score >= 5) {
            badgeColor = "bg-amber-50 text-[#D99A2B] border border-amber-200";
            border = "border-l-[#D99A2B]";
        }

        const keyBadges = n.keywords_found.split(',')
            .map(k => k.trim())
            .filter(k => k)
            .map(k => `<span class="bg-[#F5F3EE] text-slate-700 text-[10px] font-mono font-bold px-2 py-0.5 rounded border border-[#E2DFD7]">${k}</span>`)
            .join(' ');

        grid.innerHTML += `
            <div class="p-5 rounded bg-white border border-[#E2DFD7] border-l-4 ${border} flex flex-col justify-between space-y-3 shadow-sm">
                <div>
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-xs text-slate-600 font-mono font-bold">📅 ${n.related_date}</span>
                        <span class="text-xs font-black font-mono px-2.5 py-0.5 rounded border ${badgeColor}">Severity: ${n.severity_score} / 15</span>
                    </div>
                    <p class="text-xs font-medium italic text-slate-900 leading-relaxed">"${n.snippet_preview}"</p>
                </div>
                <div class="border-t border-[#E2DFD7] pt-2.5">
                    <div class="text-[10px] font-bold text-slate-600 uppercase tracking-wider mb-1.5 font-mono">Extracted Tags</div>
                    <div class="flex flex-wrap gap-1">${keyBadges}</div>
                </div>
            </div>
        `;
    });
}

// Fetch daily rainfall and render EDA charts
async function loadInsights() {
    let data;
    try {
        const response = await fetch(`${API_BASE}/api/historical`);
        const json = await response.json();
        if (response.ok && Array.isArray(json)) {
            data = json;
        }
    } catch (e) {
        console.warn("Backend API unavailable, using local embedded historical dataset.");
    }
    if (!data || !Array.isArray(data)) {
        data = FALLBACK_HISTORICAL;
    }

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
        const mName = months[d.month] || 'July';
        if (!boxData[mName]) boxData[mName] = [];
        boxData[mName].push(d.rainfall_mm);
    });

    const boxTraces = Object.keys(boxData).map(m => ({
        y: boxData[m],
        name: m,
        type: 'box',
        boxpoints: 'outliers',
        marker: { color: m === 'July' ? COLOR_HIGH : COLOR_ACCENT }
    }));

    Plotly.newPlot('chart-month', boxTraces, {
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: { color: '#252525' },
        xaxis: { gridcolor: 'rgba(0,0,0,0.06)', linecolor: 'rgba(0,0,0,0.1)' },
        yaxis: { gridcolor: 'rgba(0,0,0,0.06)', linecolor: 'rgba(0,0,0,0.1)', title: 'Rainfall (mm)' },
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
        marker: { color: COLOR_ACCENT, size: 6, opacity: 0.6 }
    };

    const traceFlood = {
        x: floodDays.map(d => d.rainfall_mm),
        y: floodDays.map(d => d.rainfall_7day),
        mode: 'markers',
        name: 'Verified Flood Event',
        type: 'scatter',
        marker: { color: COLOR_HIGH, size: 10, line: { width: 1, color: '#fff' } }
    };

    Plotly.newPlot('chart-scatter', [traceNormal, traceFlood], {
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: { color: '#252525' },
        xaxis: { gridcolor: 'rgba(0,0,0,0.06)', linecolor: 'rgba(0,0,0,0.1)', title: 'Precipitation Intensity Today (mm)' },
        yaxis: { gridcolor: 'rgba(0,0,0,0.06)', linecolor: 'rgba(0,0,0,0.1)', title: '7-Day Soil Saturation (mm)' },
        margin: { t: 20, b: 45, l: 50, r: 20 }
    }, { responsive: true, displayModeBar: false });

    // 3. Correlation Heatmap
    const getMean = arr => arr.reduce((a,b)=>a+b,0)/arr.length;
    const getStd = (arr, mean) => Math.sqrt(arr.reduce((a,b)=>a+Math.pow(b-mean,2),0)/(arr.length-1 || 1));
    const getCorr = (x, y) => {
        const mx = getMean(x);
        const my = getMean(y);
        const sx = getStd(x, mx);
        const sy = getStd(y, my);
        let sum = 0;
        for(let i=0; i<x.length; i++) {
            sum += (x[i]-mx)*(y[i]-my);
        }
        return sum/((x.length-1 || 1)*sx*sy || 1);
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
        colorscale: 'Oranges',
        zmin: -1, zmax: 1
    };

    Plotly.newPlot('chart-corr', [traceHeat], {
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: { color: '#252525' },
        margin: { t: 20, b: 40, l: 100, r: 20 }
    }, { responsive: true, displayModeBar: false });
}

// LOGISTICS & SECTOR-WISE ECONOMIC DELAY SIMULATOR
function runEconomicSim() {
    const sev = document.getElementById('eco-severity').value;

    const lossEl = document.getElementById('eco-loss');
    const workforceEl = document.getElementById('eco-workforce');
    const failureEl = document.getElementById('eco-failure');

    // Quick Commerce Elements
    const qcBadge = document.getElementById('qc-badge');
    const qcDelay = document.getElementById('qc-delay');
    const qcStatus = document.getElementById('qc-status');
    const qcSurge = document.getElementById('qc-surge');

    // E-Commerce Elements
    const ecomBadge = document.getElementById('ecom-badge');
    const ecomDelay = document.getElementById('ecom-delay');
    const ecomStatus = document.getElementById('ecom-status');

    // Transit Elements
    const transitBadge = document.getElementById('transit-badge');
    const transitTrain = document.getElementById('transit-train');

    // Corporate Elements
    const corpWfh = document.getElementById('corp-wfh');
    const corpWage = document.getElementById('corp-wage');

    if (sev === "No_Flood") {
        if (lossEl) lossEl.innerText = "₹0.0 Crores / day";
        if (workforceEl) workforceEl.innerText = "0% Workforce Disruption";
        if (failureEl) failureEl.innerText = "0% Order Failure";

        if (qcBadge) { qcBadge.innerText = "Normal Service"; qcBadge.className = "px-2.5 py-1 rounded text-xs font-bold bg-emerald-50 text-[#5F8A6A] border border-emerald-200 font-mono"; }
        if (qcDelay) qcDelay.innerText = "10–15 Minutes (Standard)";
        if (qcStatus) qcStatus.innerText = "All Wards Fully Operational";
        if (qcSurge) qcSurge.innerText = "Standard delivery fee (No Surge)";

        if (ecomBadge) { ecomBadge.innerText = "On-Time"; ecomBadge.className = "px-2.5 py-1 rounded text-xs font-bold bg-emerald-50 text-[#5F8A6A] border border-emerald-200 font-mono"; }
        if (ecomDelay) ecomDelay.innerText = "Same-Day / Next-Day Active";
        if (ecomStatus) ecomStatus.innerText = "Bhiwandi & Kurla Hubs Clear";

        if (transitBadge) { transitBadge.innerText = "On Schedule"; transitBadge.className = "px-2.5 py-1 rounded text-xs font-bold bg-emerald-50 text-[#5F8A6A] border border-emerald-200 font-mono"; }
        if (transitTrain) transitTrain.innerText = "Local trains running on time";

        if (corpWfh) corpWfh.innerText = "Normal office attendance";
        if (corpWage) corpWage.innerText = "₹0 wage loss";
    } 
    else if (sev === "Slight") {
        if (lossEl) lossEl.innerText = "₹8.5 Crores / day";
        if (workforceEl) workforceEl.innerText = "12% Workforce Disruption";
        if (failureEl) failureEl.innerText = "5% Order Failure";

        if (qcBadge) { qcBadge.innerText = "Minor Delays"; qcBadge.className = "px-2.5 py-1 rounded text-xs font-bold bg-[#F5F3EE] text-[#D97745] border border-[#E2DFD7] font-mono"; }
        if (qcDelay) qcDelay.innerText = "25–35 Minutes (+15m delay)";
        if (qcStatus) qcStatus.innerText = "Sion & Hindmata Wards slow";
        if (qcSurge) qcSurge.innerText = "+₹15 – ₹25 Rain Surge Fee";

        if (ecomBadge) { ecomBadge.innerText = "+6h Delay"; ecomBadge.className = "px-2.5 py-1 rounded text-xs font-bold bg-[#F5F3EE] text-[#D97745] border border-[#E2DFD7] font-mono"; }
        if (ecomDelay) ecomDelay.innerText = "Same-Day deferred to next day";
        if (ecomStatus) ecomStatus.innerText = "Minor traffic bottlenecks at Hubs";

        if (transitBadge) { transitBadge.innerText = "10-min Delays"; transitBadge.className = "px-2.5 py-1 rounded text-xs font-bold bg-[#F5F3EE] text-[#D97745] border border-[#E2DFD7] font-mono"; }
        if (transitTrain) transitTrain.innerText = "10–15 min delays on Harbour Line";

        if (corpWfh) corpWfh.innerText = "25% Staff WFH advisory";
        if (corpWage) corpWage.innerText = "₹1.8 Crores lost wages";
    } 
    else if (sev === "Moderate") {
        if (lossEl) lossEl.innerText = "₹48.0 Crores / day";
        if (workforceEl) workforceEl.innerText = "42% Workforce Disruption";
        if (failureEl) failureEl.innerText = "28% Order Failure";

        if (qcBadge) { qcBadge.innerText = "High Surge / Paused"; qcBadge.className = "px-2.5 py-1 rounded text-xs font-bold bg-amber-50 text-[#D99A2B] border border-amber-200 font-mono"; }
        if (qcDelay) qcDelay.innerText = "45–60 Minutes (+35m delay)";
        if (qcStatus) qcStatus.innerText = "Sion, Kurla & Andheri Wards Paused";
        if (qcSurge) qcSurge.innerText = "+₹35 – ₹60 Surge Fee Active";

        if (ecomBadge) { ecomBadge.innerText = "+24h Backlog"; ecomBadge.className = "px-2.5 py-1 rounded text-xs font-bold bg-amber-50 text-[#D99A2B] border border-amber-200 font-mono"; }
        if (ecomDelay) ecomDelay.innerText = "+24 Hours Delivery Backlog";
        if (ecomStatus) ecomStatus.innerText = "Bhiwandi & Kurla Hub Waterlogging";

        if (transitBadge) { transitBadge.innerText = "Subway Flooded"; transitBadge.className = "px-2.5 py-1 rounded text-xs font-bold bg-amber-50 text-[#D99A2B] border border-amber-200 font-mono"; }
        if (transitTrain) transitTrain.innerText = "25–35 min delays on Central Line";

        if (corpWfh) corpWfh.innerText = "65% IT/BFSI Staff Remote Shift";
        if (corpWage) corpWage.innerText = "₹12.5 Crores lost wages";
    } 
    else { // Severe
        if (lossEl) lossEl.innerText = "₹195.0 Crores / day";
        if (workforceEl) workforceEl.innerText = "78% Workforce Disruption";
        if (failureEl) failureEl.innerText = "70% Order Failure";

        if (qcBadge) { qcBadge.innerText = "SERVICE SUSPENDED"; qcBadge.className = "px-2.5 py-1 rounded text-xs font-bold bg-red-50 text-[#C9473D] border border-red-200 font-mono"; }
        if (qcDelay) qcDelay.innerText = "Deliveries Suspended Citywide";
        if (qcStatus) qcStatus.innerText = "All Hyperlocal Hubs Shutdown";
        if (qcSurge) qcSurge.innerText = "Service Unavailable";

        if (ecomBadge) { ecomBadge.innerText = "+48-72h Freeze"; ecomBadge.className = "px-2.5 py-1 rounded text-xs font-bold bg-red-50 text-[#C9473D] border border-red-200 font-mono"; }
        if (ecomDelay) ecomDelay.innerText = "+48 to 72 Hours Hold";
        if (ecomStatus) ecomStatus.innerText = "Inundated Warehouses (Bhiwandi)";

        if (transitBadge) { transitBadge.innerText = "TRACKS SUBMERGED"; transitBadge.className = "px-2.5 py-1 rounded text-xs font-bold bg-red-50 text-[#C9473D] border border-red-200 font-mono"; }
        if (transitTrain) transitTrain.innerText = "Local trains suspended (Kurla/Sion)";

        if (corpWfh) corpWfh.innerText = "90% Work From Home mandatory";
        if (corpWage) corpWage.innerText = "₹45.0 Crores lost daily wages";
    }
}

// Initial load triggers
window.onload = async () => {
    initGisMap();
    switchTab('map');
    runEconomicSim();
    await fetchLiveWeather();
};
