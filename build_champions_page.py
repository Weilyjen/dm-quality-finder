# -*- coding: utf-8 -*-
"""
Generate champions.html for 115Q1 Taiwan Counties & Cities Diabetes Champion Clinics
Features:
- Standalone, zero-dependency, ultra-fast modern HTML5/CSS3/ES6 web page.
- Fully responsive on mobile, tablet, desktop.
- Displays County/City and District for all 22 clinics.
- Dual View: Champion Cards Grid View & Full 20-Indicator Quality Table View.
- Region filtering (All, North, Central, South, East, Islands).
- Instant live search.
- Direct prominent CTA and links to https://weilyjen.github.io/dm-quality-finder/.
- Promotes Hierarchical Healthcare (分級醫療) & Local Care (在地就醫).
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "champions_full_data.json")
OUTPUT_HTML = os.path.join(BASE_DIR, "champions.html")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    payload = json.load(f)

clinics = payload["clinics"]
indicators = payload["indicators"]

# Generate JSON string to embed in the page
embedded_json = json.dumps(payload, ensure_ascii=False)

html_template = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>115Q1 台灣各縣市糖尿病收案冠軍診所名單 — 分級醫療·在地就醫</title>
  <meta name="description" content="健保署115年Q1官方公開品質評比：全台22縣市糖尿病收案人數第一名基層診所排行榜。落實分級醫療，免奔波大醫院，在地優質照護安心就醫。">
  <meta name="keywords" content="糖尿病, 診所冠軍, 分級醫療, 在地就醫, 健保品質, 115Q1, 游能俊診所, 安慎診所, 文德診所, 糖尿病照護方案">

  <!-- Open Graph Meta -->
  <meta property="og:title" content="115Q1 台灣各縣市糖尿病收案冠軍診所名單 — 分級醫療·在地就醫">
  <meta property="og:description" content="全台22縣市糖尿病基層診所第一名冠軍榜！收案人數破千、照護率超高、定期檢驗落實率超越醫學中心。就近在地就醫，查閱身邊頂尖糖病守護者。">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://weilyjen.github.io/dm-quality-finder/champions.html">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;600;700;800;900&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    :root {{
      --primary: #0d9488;
      --primary-hover: #0f766e;
      --primary-light: #ccfbf1;
      --primary-dark: #115e59;
      --primary-glow: rgba(13, 148, 136, 0.25);
      
      --gold: #d97706;
      --gold-light: #fef3c7;
      --gold-dark: #b45309;
      --gold-gradient: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
      --gold-glow: rgba(245, 158, 11, 0.3);
      
      --secondary: #2563eb;
      --secondary-light: #dbeafe;
      --accent: #f59e0b;
      --success: #10b981;
      --success-light: #ecfdf5;
      
      --bg: #f8fafc;
      --card-bg: rgba(255, 255, 255, 0.96);
      --card-border: #e2e8f0;
      --text: #0f172a;
      --text-muted: #64748b;
      --text-sub: #334155;
      
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.08), 0 2px 4px -2px rgb(0 0 0 / 0.05);
      --shadow-lg: 0 10px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.05);
      --shadow-xl: 0 20px 35px -10px rgb(0 0 0 / 0.15);
      
      --radius: 16px;
      --radius-sm: 10px;
      --radius-full: 9999px;
      --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    [data-theme="dark"] {{
      --bg: #090d16;
      --card-bg: rgba(22, 28, 45, 0.92);
      --card-border: #2e384d;
      --text: #f1f5f9;
      --text-muted: #94a3b8;
      --text-sub: #cbd5e1;
      --primary-light: rgba(13, 148, 136, 0.2);
      --gold-light: rgba(245, 158, 11, 0.18);
      --secondary-light: rgba(37, 99, 235, 0.2);
      --success-light: rgba(16, 185, 129, 0.18);
      --shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
      --shadow-lg: 0 12px 32px rgba(0, 0, 0, 0.6);
      --shadow-xl: 0 20px 40px rgba(0, 0, 0, 0.7);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    
    body {{
      font-family: 'Outfit', 'Noto Sans TC', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      min-height: 100vh;
      transition: background-color 0.3s ease, color 0.3s ease;
      -webkit-font-smoothing: antialiased;
    }}

    /* Header */
    header {{
      position: sticky;
      top: 0;
      z-index: 50;
      background: var(--card-bg);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--card-border);
      padding: 12px 24px;
      transition: var(--transition);
    }}
    .header-inner {{
      max-width: 1280px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: inherit;
    }}
    .brand-icon {{
      width: 44px;
      height: 44px;
      border-radius: var(--radius-sm);
      background: var(--gold-gradient);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-size: 24px;
      box-shadow: 0 4px 12px var(--gold-glow);
    }}
    .brand-text {{
      display: flex;
      flex-direction: column;
    }}
    .brand-title {{
      font-size: 1.15rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .brand-badge {{
      font-size: 0.72rem;
      font-weight: 700;
      background: var(--gold-light);
      color: var(--gold-dark);
      padding: 2px 8px;
      border-radius: var(--radius-full);
      border: 1px solid rgba(245, 158, 11, 0.3);
    }}
    .brand-sub {{
      font-size: 0.78rem;
      color: var(--text-muted);
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .btn-main-app {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: linear-gradient(135deg, var(--primary) 0%, var(--primary-hover) 100%);
      color: #ffffff !important;
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 8px 16px;
      border-radius: var(--radius-full);
      box-shadow: 0 4px 12px var(--primary-glow);
      transition: var(--transition);
    }}
    .btn-main-app:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 18px var(--primary-glow);
    }}
    .btn-icon-round {{
      width: 38px;
      height: 38px;
      border-radius: var(--radius-full);
      border: 1px solid var(--card-border);
      background: var(--card-bg);
      color: var(--text-sub);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 16px;
      transition: var(--transition);
    }}
    .btn-icon-round:hover {{
      background: var(--primary-light);
      color: var(--primary);
      border-color: var(--primary);
    }}

    /* Main Container */
    .container {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 28px 20px 80px;
    }}

    /* Hero Banner */
    .hero-banner {{
      position: relative;
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0d9488 100%);
      color: #ffffff;
      padding: 36px 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow-xl);
      overflow: hidden;
      margin-bottom: 28px;
    }}
    .hero-banner::before {{
      content: "🏆";
      position: absolute;
      right: 20px;
      bottom: -30px;
      font-size: 180px;
      opacity: 0.12;
      pointer-events: none;
      user-select: none;
    }}
    .hero-tag-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 14px;
    }}
    .hero-tag {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 12px;
      border-radius: var(--radius-full);
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.03em;
    }}
    .tag-gold {{
      background: rgba(245, 158, 11, 0.25);
      color: #fbbf24;
      border: 1px solid rgba(245, 158, 11, 0.4);
    }}
    .tag-teal {{
      background: rgba(13, 148, 136, 0.25);
      color: #5eead4;
      border: 1px solid rgba(13, 148, 136, 0.4);
    }}
    .tag-blue {{
      background: rgba(37, 99, 235, 0.25);
      color: #93c5fd;
      border: 1px solid rgba(37, 99, 235, 0.4);
    }}

    .hero-title {{
      font-size: 2.1rem;
      font-weight: 900;
      line-height: 1.25;
      margin-bottom: 12px;
      letter-spacing: -0.02em;
    }}
    .hero-title span {{
      background: linear-gradient(135deg, #fde68a 0%, #f59e0b 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero-desc {{
      font-size: 1.05rem;
      color: #cbd5e1;
      max-width: 820px;
      line-height: 1.65;
      margin-bottom: 24px;
    }}
    .hero-desc strong {{
      color: #ffffff;
    }}

    /* Stat Highlight Cards */
    .hero-stats {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
      gap: 14px;
      margin-bottom: 24px;
    }}
    .hero-stat-card {{
      background: rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-sm);
      padding: 14px 18px;
    }}
    .stat-label {{
      font-size: 0.78rem;
      color: #94a3b8;
      margin-bottom: 4px;
      font-weight: 500;
    }}
    .stat-val {{
      font-size: 1.6rem;
      font-weight: 800;
      color: #f8fafc;
      font-family: 'Outfit', sans-serif;
    }}
    .stat-val small {{
      font-size: 0.85rem;
      font-weight: 600;
      color: #cbd5e1;
      margin-left: 2px;
    }}
    .stat-badge {{
      font-size: 0.72rem;
      color: #5eead4;
      font-weight: 600;
    }}

    /* Big Hero CTA Callout */
    .hero-cta-callout {{
      background: rgba(13, 148, 136, 0.2);
      border: 1px solid rgba(94, 234, 212, 0.35);
      border-radius: var(--radius-sm);
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
    }}
    .cta-text-wrap {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}
    .cta-icon {{
      font-size: 32px;
      flex-shrink: 0;
    }}
    .cta-title {{
      font-size: 1.05rem;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 2px;
    }}
    .cta-sub {{
      font-size: 0.85rem;
      color: #cbd5e1;
    }}
    .cta-btn-link {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #ffffff;
      color: #0f766e !important;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 10px 22px;
      border-radius: var(--radius-full);
      text-decoration: none;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
      transition: var(--transition);
      white-space: nowrap;
    }}
    .cta-btn-link:hover {{
      transform: scale(1.03);
      background: #f0fdfa;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);
    }}

    /* Control Toolbar */
    .toolbar {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: 16px 20px;
      margin-bottom: 24px;
      box-shadow: var(--shadow);
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}
    .toolbar-row-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .region-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .region-pill {{
      border: 1px solid var(--card-border);
      background: var(--bg);
      color: var(--text-sub);
      padding: 6px 14px;
      border-radius: var(--radius-full);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition);
    }}
    .region-pill:hover {{
      border-color: var(--primary);
      color: var(--primary);
    }}
    .region-pill.active {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      box-shadow: 0 2px 8px var(--primary-glow);
    }}

    .view-toggles {{
      display: flex;
      background: var(--bg);
      padding: 3px;
      border-radius: var(--radius-full);
      border: 1px solid var(--card-border);
    }}
    .view-toggle-btn {{
      padding: 6px 14px;
      border-radius: var(--radius-full);
      font-size: 0.82rem;
      font-weight: 700;
      border: none;
      background: transparent;
      color: var(--text-muted);
      cursor: pointer;
      transition: var(--transition);
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .view-toggle-btn.active {{
      background: var(--card-bg);
      color: var(--text);
      box-shadow: var(--shadow-sm);
    }}

    /* Search and Result Count */
    .toolbar-row-bottom {{
      display: flex;
      align-items: center;
      gap: 12px;
      justify-content: space-between;
    }}
    .search-box {{
      position: relative;
      flex: 1;
      max-width: 460px;
    }}
    .search-box input {{
      width: 100%;
      padding: 10px 16px 10px 42px;
      border-radius: var(--radius-full);
      border: 1px solid var(--card-border);
      background: var(--bg);
      color: var(--text);
      font-size: 0.9rem;
      outline: none;
      transition: var(--transition);
    }}
    .search-box input:focus {{
      border-color: var(--primary);
      background: var(--card-bg);
      box-shadow: 0 0 0 3px var(--primary-light);
    }}
    .search-icon {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      font-size: 16px;
      pointer-events: none;
    }}
    .result-stats {{
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: 500;
    }}
    .result-stats strong {{
      color: var(--primary);
    }}

    /* Cards Grid View */
    .cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 20px;
    }}
    .champion-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: 22px;
      box-shadow: var(--shadow);
      transition: var(--transition);
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
    }}
    .champion-card:hover {{
      transform: translateY(-4px);
      box-shadow: var(--shadow-lg);
      border-color: rgba(13, 148, 136, 0.4);
    }}
    .champion-card.rank-1 {{
      border: 2px solid #f59e0b;
      box-shadow: 0 8px 24px var(--gold-glow);
    }}
    .champion-card.rank-1::after {{
      content: "全國總冠軍";
      position: absolute;
      top: 18px;
      right: -32px;
      transform: rotate(45deg);
      background: var(--gold-gradient);
      color: #ffffff;
      font-size: 0.68rem;
      font-weight: 800;
      padding: 4px 34px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    }}

    .card-top-row {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 12px;
    }}
    .location-tags {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }}
    .city-badge {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 800;
      font-size: 0.82rem;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
    }}
    .district-badge {{
      background: var(--bg);
      border: 1px solid var(--card-border);
      color: var(--text-sub);
      font-weight: 700;
      font-size: 0.78rem;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
    }}
    .rank-pill {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 0.75rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: var(--radius-full);
      background: var(--gold-light);
      color: var(--gold-dark);
    }}

    .clinic-title-wrap {{
      margin-bottom: 16px;
    }}
    .clinic-name {{
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--text);
      line-height: 1.3;
      margin-bottom: 4px;
    }}
    .clinic-meta {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.78rem;
      color: var(--text-muted);
    }}
    .clinic-code {{
      font-family: 'Outfit', monospace;
      font-weight: 600;
      background: var(--bg);
      padding: 1px 6px;
      border-radius: 4px;
      border: 1px solid var(--card-border);
    }}

    /* Metrics Grid Inside Card */
    .metrics-grid {{
      background: var(--bg);
      border-radius: var(--radius-sm);
      border: 1px solid var(--card-border);
      padding: 12px;
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
      margin-bottom: 16px;
    }}
    .metric-cell {{
      display: flex;
      flex-direction: column;
    }}
    .metric-label {{
      font-size: 0.72rem;
      color: var(--text-muted);
      margin-bottom: 2px;
      font-weight: 500;
    }}
    .metric-val {{
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--text);
      font-family: 'Outfit', sans-serif;
      display: flex;
      align-items: baseline;
      gap: 4px;
    }}
    .metric-val.highlight {{
      color: var(--primary);
    }}
    .metric-sub {{
      font-size: 0.72rem;
      color: var(--text-muted);
    }}

    /* Clinical Rates Mini Bar */
    .clinical-rates-list {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-bottom: 18px;
    }}
    .rate-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.8rem;
    }}
    .rate-name {{
      color: var(--text-sub);
      display: flex;
      align-items: center;
      gap: 6px;
      font-weight: 500;
    }}
    .rate-score {{
      font-weight: 700;
      font-family: 'Outfit', sans-serif;
    }}
    .score-badge {{
      display: inline-block;
      padding: 1px 6px;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 700;
    }}
    .score-badge.high {{
      background: var(--success-light);
      color: var(--success);
    }}
    .score-badge.normal {{
      background: var(--bg);
      border: 1px solid var(--card-border);
      color: var(--text-sub);
    }}

    /* Card Action Footer */
    .card-footer {{
      margin-top: auto;
      padding-top: 14px;
      border-top: 1px solid var(--card-border);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .btn-card-nhi {{
      flex: 1;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      background: var(--bg);
      border: 1px solid var(--card-border);
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.78rem;
      font-weight: 600;
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      transition: var(--transition);
    }}
    .btn-card-nhi:hover {{
      background: var(--primary-light);
      color: var(--primary);
      border-color: var(--primary);
    }}
    .btn-card-compare {{
      flex: 1.2;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      background: var(--primary);
      color: #ffffff !important;
      text-decoration: none;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      transition: var(--transition);
    }}
    .btn-card-compare:hover {{
      background: var(--primary-hover);
      box-shadow: 0 4px 10px var(--primary-glow);
    }}

    /* Table View */
    .table-container {{
      display: none;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      overflow: hidden;
      margin-bottom: 24px;
    }}
    .table-container.active {{
      display: block;
    }}
    .table-scroll {{
      overflow-x: auto;
      max-height: 75vh;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
      text-align: left;
    }}
    thead th {{
      position: sticky;
      top: 0;
      background: var(--bg);
      z-index: 10;
      padding: 12px 14px;
      border-bottom: 2px solid var(--card-border);
      font-weight: 700;
      white-space: nowrap;
    }}
    thead th.th-fixed {{
      left: 0;
      z-index: 20;
      background: var(--bg);
      border-right: 1px solid var(--card-border);
    }}
    .th-clinic-box {{
      min-width: 190px;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}
    .th-clinic-city {{
      font-size: 0.75rem;
      color: var(--primary);
      font-weight: 800;
    }}
    .th-clinic-name {{
      font-size: 0.95rem;
      font-weight: 800;
      color: var(--text);
    }}
    .th-clinic-sub {{
      font-size: 0.72rem;
      color: var(--text-muted);
      font-weight: normal;
    }}

    tbody td {{
      padding: 12px 14px;
      border-bottom: 1px solid var(--card-border);
      vertical-align: middle;
    }}
    tbody td.td-fixed {{
      position: sticky;
      left: 0;
      background: var(--card-bg);
      z-index: 5;
      font-weight: 600;
      border-right: 1px solid var(--card-border);
      min-width: 220px;
    }}
    tbody tr:hover td {{
      background: var(--bg);
    }}
    .td-metric-cat {{
      font-size: 0.7rem;
      color: var(--text-muted);
      display: block;
      margin-bottom: 2px;
    }}
    .td-metric-title {{
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--text);
    }}
    .td-metric-period {{
      font-size: 0.72rem;
      color: var(--text-muted);
      display: block;
    }}
    .table-cell-val {{
      text-align: center;
      font-family: 'Outfit', sans-serif;
    }}
    .table-val-bold {{
      font-weight: 700;
      color: var(--text);
    }}
    .table-badge-rate {{
      display: inline-block;
      padding: 1px 6px;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 700;
      background: var(--success-light);
      color: var(--success);
      margin-top: 2px;
    }}

    /* Education & FAQ Section */
    .edu-section {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: 32px 28px;
      margin-top: 36px;
      box-shadow: var(--shadow);
    }}
    .edu-header {{
      text-align: center;
      max-width: 700px;
      margin: 0 auto 28px;
    }}
    .edu-header h2 {{
      font-size: 1.65rem;
      font-weight: 800;
      margin-bottom: 8px;
      color: var(--text);
    }}
    .edu-header p {{
      font-size: 0.92rem;
      color: var(--text-muted);
    }}

    .edu-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin-bottom: 28px;
    }}
    .edu-card {{
      background: var(--bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-sm);
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .edu-icon {{
      font-size: 32px;
      margin-bottom: 4px;
    }}
    .edu-card h3 {{
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--primary);
    }}
    .edu-card p {{
      font-size: 0.88rem;
      color: var(--text-sub);
      line-height: 1.6;
    }}

    /* Banner Bottom Link */
    .finder-callout-bottom {{
      background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
      color: #ffffff;
      padding: 28px;
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 20px;
      margin-top: 20px;
    }}
    .finder-callout-bottom h3 {{
      font-size: 1.3rem;
      font-weight: 800;
      margin-bottom: 4px;
    }}
    .finder-callout-bottom p {{
      font-size: 0.9rem;
      opacity: 0.9;
    }}

    /* Footer */
    footer {{
      border-top: 1px solid var(--card-border);
      background: var(--card-bg);
      padding: 32px 20px;
      margin-top: 40px;
      color: var(--text-muted);
      font-size: 0.82rem;
      line-height: 1.7;
    }}
    .footer-inner {{
      max-width: 1280px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
    }}
    .footer-links a {{
      color: var(--primary);
      text-decoration: none;
      font-weight: 600;
    }}
    .footer-links a:hover {{
      text-decoration: underline;
    }}

    /* Responsive */
    @media (max-width: 768px) {{
      .hero-title {{ font-size: 1.55rem; }}
      .hero-banner {{ padding: 24px 20px; }}
      .cards-grid {{ grid-template-columns: 1fr; }}
      .header-actions .brand-sub {{ display: none; }}
      .btn-main-app span {{ display: none; }}
      .btn-main-app {{ padding: 8px 12px; }}
      .toolbar {{ padding: 12px 14px; }}
    }}
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="header-inner">
      <a href="https://weilyjen.github.io/dm-quality-finder/" class="brand">
        <div class="brand-icon">🏆</div>
        <div class="brand-text">
          <div class="brand-title">
            各縣市冠軍診所榜
            <span class="brand-badge">115Q1 官方最新</span>
          </div>
          <div class="brand-sub">全台糖尿病院所品質查詢器專題</div>
        </div>
      </a>

      <div class="header-actions">
        <a href="https://weilyjen.github.io/dm-quality-finder/" class="btn-main-app" title="前往全台糖尿病院所即時查詢器">
          <span>🔍 查閱全台 7,765 家院所</span>
          <span>➜</span>
        </a>
        <button id="themeToggle" class="btn-icon-round" title="切換深色/淺色主題">🌓</button>
      </div>
    </div>
  </header>

  <!-- Container -->
  <main class="container">

    <!-- Hero Banner -->
    <section class="hero-banner">
      <div class="hero-tag-row">
        <span class="hero-tag tag-gold">👑 115Q1 全台 22 縣市收案第一名</span>
        <span class="hero-tag tag-teal">🩺 衛生福利部中央健康保險署官方指標</span>
        <span class="hero-tag tag-blue">🏥 推動分級醫療 · 鼓勵在地就醫</span>
      </div>

      <h1 class="hero-title">
        115Q1 台灣各縣市<span>糖尿病收案人數冠軍診所</span>名單
      </h1>
      
      <p class="hero-desc">
        <strong>「大病到大醫院，慢性病在社區好診所」</strong>。健保署統計數據證實：台灣各縣市基層專科診所具備強大的照護量能與卓越醫療品質！醣化血紅素追蹤率普遍超過 <strong>99%</strong>、尿蛋白與眼底檢查執行率超越 <strong>90%~95%</strong>。糖友免奔波大醫院，在地就醫就能享受完整醫療團隊長期照護！
      </p>

      <!-- Stats Grid -->
      <div class="hero-stats">
        <div class="hero-stat-card">
          <div class="stat-label">評比縣市覆蓋</div>
          <div class="stat-val">22 <small>縣市</small></div>
          <div class="stat-badge">100% 台灣全島與離島</div>
        </div>
        <div class="hero-stat-card">
          <div class="stat-label">22 院所累計收案</div>
          <div class="stat-val">35,496 <small>人</small></div>
          <div class="stat-badge">基層專科強大能量</div>
        </div>
        <div class="hero-stat-card">
          <div class="stat-label">平均照護方案加入率</div>
          <div class="stat-val">82.6<small>%</small></div>
          <div class="stat-badge">最高達 95.2%</div>
        </div>
        <div class="hero-stat-card">
          <div class="stat-label">HbA1c 糖化血色素率</div>
          <div class="stat-val">99.2<small>%</small></div>
          <div class="stat-badge">品質超越醫學中心</div>
        </div>
      </div>

      <!-- Big CTA -->
      <div class="hero-cta-callout">
        <div class="cta-text-wrap">
          <div class="cta-icon">🗺️</div>
          <div>
            <div class="cta-title">想找您家附近的糖尿病照護院所嗎？</div>
            <div class="cta-sub">立即前往「全台糖尿病院所品質查詢器」，按您的縣市、鄉鎮市區一鍵查詢 7,765 家院所品質！</div>
          </div>
        </div>
        <a href="https://weilyjen.github.io/dm-quality-finder/" class="cta-btn-link">
          前往全台即時查詢器 ➜
        </a>
      </div>
    </section>

    <!-- Toolbar -->
    <section class="toolbar">
      <div class="toolbar-row-top">
        <div class="region-pills" id="regionPills">
          <button class="region-pill active" data-region="all">全部縣市 (22)</button>
          <button class="region-pill" data-region="北部">北部 (7)</button>
          <button class="region-pill" data-region="中部">中部 (5)</button>
          <button class="region-pill" data-region="南部">南部 (5)</button>
          <button class="region-pill" data-region="東部">東部 (2)</button>
          <button class="region-pill" data-region="離島">離島 (3)</button>
        </div>

        <div class="view-toggles">
          <button class="view-toggle-btn active" id="viewCardsBtn">
            <span>🎴</span> 精選卡片
          </button>
          <button class="view-toggle-btn" id="viewTableBtn">
            <span>📊</span> 完整品質表
          </button>
        </div>
      </div>

      <div class="toolbar-row-bottom">
        <div class="search-box">
          <span class="search-icon">🔍</span>
          <input type="text" id="searchInput" placeholder="搜尋縣市（如 宜蘭、新北）、鄉鎮區（如 羅東、鹿港）、診所名或代碼...">
        </div>
        <div class="result-stats">
          顯示 <strong id="visibleCount">22</strong> 家縣市冠軍
        </div>
      </div>
    </section>

    <!-- Cards Grid Container -->
    <section class="cards-grid" id="cardsGrid">
      <!-- Populated dynamically via JS -->
    </section>

    <!-- Table Container -->
    <section class="table-container" id="tableContainer">
      <div class="table-scroll">
        <table id="qualityTable">
          <!-- Populated dynamically via JS -->
        </table>
      </div>
    </section>

    <!-- Education & Guidelines for Hierarchical Healthcare -->
    <section class="edu-section">
      <div class="edu-header">
        <h2>🏥 為什麼推薦糖尿病友「分級醫療、在地就醫」？</h2>
        <p>慢性病照護的核心在於「長期、可近、專業與夥伴關係」。基層診所為病友帶來的四大關鍵優勢：</p>
      </div>

      <div class="edu-grid">
        <div class="edu-card">
          <div class="edu-icon">⏱️</div>
          <h3>免去排隊奔波，就醫更輕鬆</h3>
          <p>不必一早就到大醫院舟車勞頓、苦候看診、等待抽血與領藥。社區診所隨到隨看，看診動線順暢，讓回診不再是沉重的負擔。</p>
        </div>

        <div class="edu-card">
          <div class="edu-icon">🩺</div>
          <h3>專屬團隊夥伴，長期陪伴控糖</h3>
          <p>糖尿病照護網基層診所由固定的專科醫師、糖尿病衛教師、營養師組成一對一團隊，深切了解您的飲食生活型態與家庭支持。</p>
        </div>

        <div class="edu-card">
          <div class="edu-icon">🔬</div>
          <h3>定期檢查全覆蓋，品質毫不遜色</h3>
          <p>健保署官方數據證實：基層冠軍診所的糖化血紅素 (HbA1c)、眼底檢查 (EYE)、尿蛋白 (ACR) 定期執行率普遍突破 90%~99%，設備與準繩齊全。</p>
        </div>

        <div class="edu-card">
          <div class="edu-icon">💰</div>
          <h3>降低健保部分負擔，實惠安心</h3>
          <p>依全民健保分級醫療政策，診所門診部分負擔大幅低於醫學中心與區域醫院，慢連箋釋出至社區藥局更享調劑便利與專業諮詢。</p>
        </div>
      </div>

      <div class="finder-callout-bottom">
        <div>
          <h3>尋找身邊優質慢病診所？</h3>
          <p>「全台糖尿病院所品質查詢器」收錄全台 7,765 家院所完整指標，支援各鄉鎮市區比對與多院所橫向評比！</p>
        </div>
        <a href="https://weilyjen.github.io/dm-quality-finder/" class="cta-btn-link">
          立即打開全台查詢器 ➜
        </a>
      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer>
    <div class="footer-inner">
      <div class="footer-links">
        <a href="https://weilyjen.github.io/dm-quality-finder/">🏠 全台糖尿病院所品質查詢器首頁</a>
        <a href="https://info.nhi.gov.tw/INAE1000/Query3LinkDetail" target="_blank" rel="noopener">🌐 健保署醫療品質資訊公開網</a>
        <a href="https://www.nhi.gov.tw" target="_blank" rel="noopener">🏛️ 衛生福利部中央健康保險署</a>
      </div>
      <div>
        <strong>資料聲明與說明</strong>：本網頁數據全數轉載自衛生福利部中央健康保險署「全民健康保險醫療品質資訊公開網」最新統計期別（115年第1季）。本專題旨在推廣分級醫療與在地就醫理念，所有指標皆客觀呈現官方申報數據。
      </div>
      <div>
        © 2026 萬華衛康內科診所醫療團隊 · 糖尿病優質照護公益推廣 · 資料即時同步自健保署公開數據庫
      </div>
    </div>
  </footer>

  <!-- Embedded Data & Interactive App Script -->
  <script>
    const APP_DATA = {embedded_json};
    const clinics = APP_DATA.clinics;
    const indicators = APP_DATA.indicators;

    // State
    let currentRegion = 'all';
    let searchQuery = '';
    let currentView = 'cards';

    // DOM Elements
    const cardsGrid = document.getElementById('cardsGrid');
    const tableContainer = document.getElementById('tableContainer');
    const qualityTable = document.getElementById('qualityTable');
    const searchInput = document.getElementById('searchInput');
    const visibleCount = document.getElementById('visibleCount');
    const regionPills = document.getElementById('regionPills');
    const viewCardsBtn = document.getElementById('viewCardsBtn');
    const viewTableBtn = document.getElementById('viewTableBtn');
    const themeToggle = document.getElementById('themeToggle');

    // Theme Switcher
    function initTheme() {{
      const savedTheme = localStorage.getItem('theme') || 'light';
      document.documentElement.setAttribute('data-theme', savedTheme);
    }}
    themeToggle.addEventListener('click', () => {{
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
    }});
    initTheme();

    // Filter Logic
    function getFilteredClinics() {{
      return clinics.filter(c => {{
        const matchRegion = (currentRegion === 'all' || c.region === currentRegion);
        if (!matchRegion) return false;
        if (!searchQuery) return true;
        const q = searchQuery.toLowerCase().trim();
        return (
          c.city.toLowerCase().includes(q) ||
          c.district.toLowerCase().includes(q) ||
          c.name.toLowerCase().includes(q) ||
          c.id.includes(q)
        );
      }});
    }}

    // Render Cards
    function renderCards() {{
      const list = getFilteredClinics();
      visibleCount.textContent = list.length;

      if (list.length === 0) {{
        cardsGrid.innerHTML = `
          <div style="grid-column: 1/-1; text-align: center; padding: 60px 20px; background: var(--card-bg); border-radius: var(--radius); border: 1px solid var(--card-border);">
            <div style="font-size: 48px; margin-bottom: 12px;">🔍</div>
            <h3 style="font-size: 1.2rem; font-weight: 800; margin-bottom: 6px;">查無符合條件的冠軍院所</h3>
            <p style="color: var(--text-muted); font-size: 0.9rem;">請嘗試更換篩選分區或搜尋其他關鍵字（例如縣市名、鄉鎮名）。</p>
          </div>
        `;
        return;
      }}

      cardsGrid.innerHTML = list.map(c => {{
        const isTop1 = (c.champion_rank === 1);
        const rankMedal = c.champion_rank === 1 ? '🥇 全國第一' :
                          c.champion_rank === 2 ? '🥈 全國第二' :
                          c.champion_rank === 3 ? '🥉 全國第三' : `全國第 ${{c.champion_rank}} 名`;

        // Extract key metrics
        const mHb = c.metrics['*HbA1c或GA (醣化血紅素/白蛋白)'] || {{}};
        const mAcr = c.metrics['*ACR (尿液微量白蛋白)'] || {{}};
        const mEye = c.metrics['*EYE (眼底檢查或攝影)'] || {{}};
        const mRelease = c.metrics['慢性病連續處方箋釋出率'] || {{}};

        return `
          <div class="champion-card ${{isTop1 ? 'rank-1' : ''}}">
            <div class="card-top-row">
              <div class="location-tags">
                <span class="city-badge">${{c.city}}冠軍</span>
                <span class="district-badge">📍 ${{c.district}}</span>
              </div>
              <span class="rank-pill">${{rankMedal}}</span>
            </div>

            <div class="clinic-title-wrap">
              <h2 class="clinic-name">${{c.name}}</h2>
              <div class="clinic-meta">
                <span>醫事代碼:</span>
                <span class="clinic-code">${{c.id}}</span>
                <span>· ${{c.type}}</span>
              </div>
            </div>

            <div class="metrics-grid">
              <div class="metric-cell">
                <span class="metric-label">115Q1 收案人數</span>
                <div class="metric-val highlight">${{c.enrolled.toLocaleString()}} <small>人</small></div>
                <span class="metric-sub">符合資格: ${{c.eligible.toLocaleString()}}人</span>
              </div>

              <div class="metric-cell">
                <span class="metric-label">照護方案加入率</span>
                <div class="metric-val">${{c.rate}}%</div>
                <span class="metric-sub">${{c.rate >= 85 ? '🌟 高收案率' : '穩健照護'}}</span>
              </div>

              <div class="metric-cell">
                <span class="metric-label">糖化血色素 HbA1c</span>
                <div class="metric-val">${{mHb.rate ? mHb.rate + '%' : (mHb.display || '—')}}</div>
                <span class="metric-sub">追蹤分子: ${{mHb.num || '—'}}人</span>
              </div>

              <div class="metric-cell">
                <span class="metric-label">慢連箋釋出率</span>
                <div class="metric-val">${{mRelease.rate ? mRelease.rate + '%' : (mRelease.display || '—')}}</div>
                <span class="metric-sub">社區藥局領藥</span>
              </div>
            </div>

            <div class="clinical-rates-list">
              <div class="rate-row">
                <span class="rate-name">🔬 尿液微量白蛋白 (ACR)</span>
                <span class="rate-score score-badge ${{parseFloat(mAcr.rate) >= 90 ? 'high' : 'normal'}}">
                  ${{mAcr.display || '—'}}
                </span>
              </div>
              <div class="rate-row">
                <span class="rate-name">👁️ 視網膜眼底檢查 (EYE)</span>
                <span class="rate-score score-badge ${{parseFloat(mEye.rate) >= 90 ? 'high' : 'normal'}}">
                  ${{mEye.display || '—'}}
                </span>
              </div>
            </div>

            <div class="card-footer">
              <a href="${{c.nhi_url}}" target="_blank" rel="noopener" class="btn-card-nhi" title="前往健保署查看詳細公開數據">
                🔗 健保署官方網頁
              </a>
              <a href="https://weilyjen.github.io/dm-quality-finder/?q=${{encodeURIComponent(c.name)}}" target="_blank" class="btn-card-compare" title="在全台查詢器中比對此院所">
                🔍 在查詢器中比對
              </a>
            </div>
          </div>
        `;
      }}).join('');
    }}

    // Render Table
    function renderTable() {{
      const list = getFilteredClinics();
      visibleCount.textContent = list.length;

      if (list.length === 0) {{
        qualityTable.innerHTML = `<tr><td colspan="5" style="text-align:center; padding:40px;">查無符合院所</td></tr>`;
        return;
      }}

      // Table Header
      let theadHtml = `
        <thead>
          <tr>
            <th class="th-fixed">
              <div style="min-width: 200px;">
                <div style="font-size: 0.78rem; color: var(--text-muted);">健保署公開指標</div>
                <div style="font-size: 1.05rem; font-weight: 800; color: var(--primary);">20項臨床評比項目</div>
              </div>
            </th>
      `;

      list.forEach(c => {{
        theadHtml += `
          <th>
            <div class="th-clinic-box">
              <div class="th-clinic-city">${{c.city}} · ${{c.district}}</div>
              <div class="th-clinic-name">${{c.name}}</div>
              <div class="th-clinic-sub">收案 ${{c.enrolled.toLocaleString()}}人 (${{c.rate}}%)</div>
            </div>
          </th>
        `;
      }});
      theadHtml += `</tr></thead>`;

      // Table Body
      let tbodyHtml = `<tbody>`;
      indicators.forEach(ind => {{
        tbodyHtml += `
          <tr>
            <td class="td-fixed">
              <span class="td-metric-cat">${{ind.category}}</span>
              <div class="td-metric-title">${{ind.name}}</div>
              <span class="td-metric-period">統計期別: ${{ind.period}}</span>
            </td>
        `;

        list.forEach(c => {{
          const itemVal = ind.values[c.id] || {{ display: '—' }};
          const isHighRate = (itemVal.rate && parseFloat(itemVal.rate) >= 90);
          
          tbodyHtml += `
            <td class="table-cell-val">
              <div class="table-val-bold">${{itemVal.display || '—'}}</div>
              ${{itemVal.rate ? `<div class="table-badge-rate ${{isHighRate ? 'high' : ''}}">${{itemVal.rate}}%</div>` : ''}}
            </td>
          `;
        }});

        tbodyHtml += `</tr>`;
      }});
      tbodyHtml += `</tbody>`;

      qualityTable.innerHTML = theadHtml + tbodyHtml;
    }}

    // Toggle Views
    function setView(view) {{
      currentView = view;
      if (view === 'cards') {{
        viewCardsBtn.classList.add('active');
        viewTableBtn.classList.remove('active');
        cardsGrid.style.display = 'grid';
        tableContainer.classList.remove('active');
        renderCards();
      }} else {{
        viewTableBtn.classList.add('active');
        viewCardsBtn.classList.remove('active');
        cardsGrid.style.display = 'none';
        tableContainer.classList.add('active');
        renderTable();
      }}
    }}

    viewCardsBtn.addEventListener('click', () => setView('cards'));
    viewTableBtn.addEventListener('click', () => setView('table'));

    // Region Pills Event
    regionPills.addEventListener('click', (e) => {{
      const btn = e.target.closest('.region-pill');
      if (!btn) return;
      document.querySelectorAll('.region-pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentRegion = btn.dataset.region;
      if (currentView === 'cards') renderCards();
      else renderTable();
    }});

    // Search Input Event
    searchInput.addEventListener('input', (e) => {{
      searchQuery = e.target.value;
      if (currentView === 'cards') renderCards();
      else renderTable();
    }});

    // Initial render
    renderCards();
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Generated {OUTPUT_HTML} successfully! Size: {os.path.getsize(OUTPUT_HTML)} bytes")
