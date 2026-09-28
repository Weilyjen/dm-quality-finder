# -*- coding: utf-8 -*-
"""
Generate sanitized ai_team.html (全體 AI 團隊致診所院長們的公開貢獻報告 - 資安脫敏企業版)
"""
import os

OUTPUT_DIR = r"D:\Antigravity\web_dm_quality"
TARGET_HTML = os.path.join(OUTPUT_DIR, "ai_team.html")
ROOT_HTML = r"D:\Antigravity\AI_CLINIC_CONTRIBUTIONS.html"

html_content = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>萬華衛康醫療團隊 — 全體 AI 協同夥伴致院長與醫師群的公開貢獻報告</title>
  <meta name="description" content="萬華衛康內科診所多 AI 協同體系致全體院長與醫師之年度數位治理、臨床品質、資訊安全與智慧營運成果報告。">

  <!-- Open Graph Meta -->
  <meta property="og:title" content="全體 AI 團隊致院長與醫師的公開貢獻報告 — 萬華衛康醫療團隊">
  <meta property="og:description" content="零個資防線、高可用性協同、慢病照護零漏追、全天候掌中遠端遙控。探索全體 AI 夥伴如何守護診所營運與病患健康！">
  <meta property="og:type" content="website">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;600;700;800;900&family=Outfit:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">

  <style>
    :root {
      --primary: #0d9488;
      --primary-hover: #0f766e;
      --primary-light: #ccfbf1;
      --primary-dark: #115e59;
      --primary-glow: rgba(13, 148, 136, 0.25);

      --blue: #2563eb;
      --blue-light: #dbeafe;
      --purple: #7c3aed;
      --purple-light: #ede9fe;
      --amber: #f59e0b;
      --amber-light: #fef3c7;
      --emerald: #059669;
      --emerald-light: #d1fae5;
      --coral: #ea580c;
      --coral-light: #ffedd5;

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

      --radius-sm: 10px;
      --radius: 18px;
      --radius-full: 9999px;
      --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }

    [data-theme="dark"] {
      --bg: #090d16;
      --card-bg: rgba(22, 28, 45, 0.94);
      --card-border: #243048;
      --text: #f1f5f9;
      --text-muted: #94a3b8;
      --text-sub: #cbd5e1;

      --primary-light: rgba(13, 148, 136, 0.18);
      --blue-light: rgba(37, 99, 235, 0.18);
      --purple-light: rgba(124, 58, 237, 0.18);
      --amber-light: rgba(245, 158, 11, 0.18);
      --emerald-light: rgba(5, 150, 105, 0.18);
      --coral-light: rgba(234, 88, 12, 0.18);

      --shadow: 0 4px 12px rgba(0, 0, 0, 0.45);
      --shadow-lg: 0 10px 25px rgba(0, 0, 0, 0.55);
      --shadow-xl: 0 20px 40px rgba(0, 0, 0, 0.7);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Outfit', 'Noto Sans TC', system-ui, -apple-system, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.65;
      -webkit-font-smoothing: antialiased;
      transition: background-color 0.3s ease, color 0.3s ease;
      overflow-x: hidden;
    }

    /* Header */
    header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--card-border);
      transition: var(--transition);
    }
    [data-theme="dark"] header {
      background: rgba(9, 13, 22, 0.85);
    }

    .header-inner {
      max-width: 1280px;
      margin: 0 auto;
      padding: 12px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: inherit;
    }
    .brand-logo {
      width: 42px;
      height: 42px;
      border-radius: 12px;
      background: linear-gradient(135deg, var(--primary) 0%, #2563eb 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-size: 22px;
      box-shadow: 0 4px 12px var(--primary-glow);
    }
    .brand-text {
      display: flex;
      flex-direction: column;
    }
    .brand-title {
      font-size: 1.12rem;
      font-weight: 800;
      letter-spacing: -0.01em;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .brand-tag {
      font-size: 0.72rem;
      font-weight: 800;
      background: var(--primary-light);
      color: var(--primary-dark);
      padding: 2px 8px;
      border-radius: var(--radius-full);
      border: 1px solid rgba(13, 148, 136, 0.3);
    }
    .brand-sub {
      font-size: 0.78rem;
      color: var(--text-muted);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .nav-link {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-sub);
      text-decoration: none;
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      transition: var(--transition);
    }
    .nav-link:hover {
      color: var(--primary);
      background: var(--primary-light);
    }
    .btn-champions {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: linear-gradient(135deg, #f59e0b, #d97706);
      color: #fff !important;
      text-decoration: none;
      font-size: 0.84rem;
      font-weight: 800;
      padding: 7px 14px;
      border-radius: var(--radius-full);
      box-shadow: 0 3px 10px rgba(245, 158, 11, 0.35);
      transition: var(--transition);
    }
    .btn-champions:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(245, 158, 11, 0.45);
    }
    .btn-theme {
      width: 38px;
      height: 38px;
      border-radius: var(--radius-full);
      border: 1px solid var(--card-border);
      background: var(--card-bg);
      color: var(--text-sub);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 16px;
      transition: var(--transition);
    }
    .btn-theme:hover {
      background: var(--primary-light);
      color: var(--primary);
    }

    /* Container */
    .container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 32px 20px 80px;
    }

    /* Hero Section */
    .hero {
      position: relative;
      background: linear-gradient(135deg, #090e17 0%, #0f1c2e 45%, #134e4a 100%);
      color: #ffffff;
      padding: 48px 36px;
      border-radius: var(--radius);
      box-shadow: var(--shadow-xl);
      overflow: hidden;
      margin-bottom: 36px;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .hero::before {
      content: "🤖";
      position: absolute;
      right: 25px;
      bottom: -35px;
      font-size: 210px;
      opacity: 0.08;
      pointer-events: none;
      user-select: none;
    }
    .hero-badge-row {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 20px;
    }
    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 14px;
      border-radius: var(--radius-full);
      font-size: 0.8rem;
      font-weight: 700;
      backdrop-filter: blur(8px);
    }
    .badge-teal {
      background: rgba(13, 148, 136, 0.25);
      border: 1px solid rgba(13, 148, 136, 0.4);
      color: #5eead4;
    }
    .badge-gold {
      background: rgba(245, 158, 11, 0.25);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: #fde68a;
    }
    .badge-blue {
      background: rgba(37, 99, 235, 0.25);
      border: 1px solid rgba(37, 99, 235, 0.4);
      color: #93c5fd;
    }

    .hero-title {
      font-size: 2.35rem;
      font-weight: 900;
      line-height: 1.25;
      margin-bottom: 16px;
      letter-spacing: -0.02em;
    }
    .hero-title span {
      background: linear-gradient(135deg, #5eead4 0%, #93c5fd 60%, #fde68a 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .hero-lead {
      font-size: 1.08rem;
      line-height: 1.7;
      color: rgba(255, 255, 255, 0.88);
      max-width: 960px;
      margin-bottom: 28px;
    }

    /* KPI Highlights */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 16px;
      margin-top: 24px;
    }
    .kpi-card {
      background: rgba(255, 255, 255, 0.07);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-radius: var(--radius-sm);
      padding: 18px 20px;
      transition: var(--transition);
    }
    .kpi-card:hover {
      background: rgba(255, 255, 255, 0.12);
      transform: translateY(-2px);
    }
    .kpi-num {
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.95rem;
      font-weight: 800;
      color: #5eead4;
      line-height: 1.1;
      margin-bottom: 6px;
    }
    .kpi-label {
      font-size: 0.82rem;
      color: rgba(255, 255, 255, 0.72);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* Section Styles */
    .section-header {
      margin-bottom: 28px;
    }
    .section-tag {
      display: inline-block;
      font-size: 0.76rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--primary);
      margin-bottom: 6px;
    }
    .section-title {
      font-size: 1.75rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--text);
    }
    .section-desc {
      font-size: 0.95rem;
      color: var(--text-muted);
      margin-top: 4px;
    }

    /* Filter / Tab Buttons */
    .filter-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 24px;
    }
    .filter-btn {
      padding: 8px 18px;
      border-radius: var(--radius-full);
      border: 1px solid var(--card-border);
      background: var(--card-bg);
      color: var(--text-sub);
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      transition: var(--transition);
    }
    .filter-btn:hover {
      border-color: var(--primary);
      color: var(--primary);
    }
    .filter-btn.active {
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      box-shadow: 0 4px 12px var(--primary-glow);
    }

    /* AI Cards Grid */
    .ai-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 24px;
      margin-bottom: 48px;
    }

    .ai-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: 28px 24px;
      box-shadow: var(--shadow);
      transition: var(--transition);
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
    }
    .ai-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-lg);
      border-color: rgba(13, 148, 136, 0.4);
    }

    /* Card color stripes */
    .ai-card::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
    }
    .ai-card.antigravity::before { background: linear-gradient(90deg, #0d9488, #2563eb); }
    .ai-card.claude::before { background: linear-gradient(90deg, #ea580c, #f59e0b); }
    .ai-card.gemini::before { background: linear-gradient(90deg, #2563eb, #7c3aed); }
    .ai-card.chatgpt::before { background: linear-gradient(90deg, #10b981, #059669); }
    .ai-card.grok::before { background: linear-gradient(90deg, #db2777, #7c3aed); }
    .ai-card.ollama::before { background: linear-gradient(90deg, #b45309, #d97706); }

    .ai-top-row {
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 16px;
    }
    .ai-avatar {
      width: 52px;
      height: 52px;
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 26px;
      flex-shrink: 0;
      box-shadow: var(--shadow-sm);
    }
    .ai-info {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
    .ai-name-row {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .ai-name {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--text);
    }
    .ai-tag {
      font-size: 0.68rem;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      background: var(--bg);
      border: 1px solid var(--card-border);
      color: var(--text-muted);
    }
    .ai-role {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--primary);
    }

    .ai-quote {
      font-size: 0.92rem;
      font-style: italic;
      color: var(--text-sub);
      background: var(--bg);
      border-left: 3px solid var(--primary);
      padding: 12px 14px;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      margin-bottom: 18px;
      line-height: 1.55;
    }

    .ai-contrib-title {
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--text);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .ai-contrib-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 20px;
      flex-grow: 1;
    }
    .ai-contrib-list li {
      font-size: 0.88rem;
      color: var(--text-sub);
      line-height: 1.5;
      position: relative;
      padding-left: 18px;
    }
    .ai-contrib-list li::before {
      content: "✦";
      position: absolute;
      left: 0;
      top: 0;
      color: var(--primary);
      font-size: 11px;
    }
    .ai-contrib-list strong {
      color: var(--text);
    }

    .ai-tools-row {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      padding-top: 14px;
      border-top: 1px dashed var(--card-border);
    }
    .ai-tool-pill {
      font-size: 0.72rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      padding: 3px 9px;
      border-radius: var(--radius-full);
      background: var(--bg);
      color: var(--text-muted);
      border: 1px solid var(--card-border);
    }
    .ai-tier-pill {
      font-size: 0.72rem;
      font-weight: 800;
      padding: 3px 9px;
      border-radius: var(--radius-full);
      background: var(--primary-light);
      color: var(--primary-dark);
      border: 1px solid rgba(13, 148, 136, 0.3);
    }

    /* Defense Architecture Section */
    .defense-section {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius);
      padding: 36px 30px;
      box-shadow: var(--shadow);
      margin-bottom: 48px;
    }
    .defense-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 18px;
      margin-top: 24px;
    }
    .defense-card {
      background: var(--bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-sm);
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      transition: var(--transition);
      position: relative;
    }
    .defense-card:hover {
      border-color: var(--primary);
      transform: translateY(-2px);
      box-shadow: var(--shadow-sm);
    }
    .defense-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .defense-tier {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.78rem;
      font-weight: 800;
      background: var(--primary-light);
      color: var(--primary-dark);
      padding: 3px 10px;
      border-radius: var(--radius-full);
    }
    .defense-status {
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--emerald);
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .defense-title {
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--text);
    }
    .defense-desc {
      font-size: 0.86rem;
      color: var(--text-sub);
      line-height: 1.55;
    }

    /* Clinic Principles */
    .rules-section {
      margin-bottom: 48px;
    }
    .rules-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 18px;
    }
    .rule-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-sm);
      padding: 22px;
      box-shadow: var(--shadow-sm);
      transition: var(--transition);
    }
    .rule-card:hover {
      border-color: var(--primary);
      transform: translateY(-2px);
    }
    .rule-icon {
      font-size: 28px;
      margin-bottom: 12px;
    }
    .rule-title {
      font-size: 1.02rem;
      font-weight: 800;
      color: var(--text);
      margin-bottom: 8px;
    }
    .rule-desc {
      font-size: 0.86rem;
      color: var(--text-sub);
      line-height: 1.55;
    }

    /* CTA Row */
    .cta-row {
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      justify-content: center;
      margin-top: 36px;
    }
    .cta-btn-primary {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: linear-gradient(135deg, var(--primary) 0%, #2563eb 100%);
      color: #fff !important;
      text-decoration: none;
      font-size: 0.95rem;
      font-weight: 800;
      padding: 12px 26px;
      border-radius: var(--radius-full);
      box-shadow: 0 4px 14px var(--primary-glow);
      transition: var(--transition);
    }
    .cta-btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(13, 148, 136, 0.4);
    }
    .cta-btn-secondary {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--card-bg);
      color: var(--text) !important;
      border: 1px solid var(--card-border);
      text-decoration: none;
      font-size: 0.95rem;
      font-weight: 800;
      padding: 12px 24px;
      border-radius: var(--radius-full);
      box-shadow: var(--shadow-sm);
      transition: var(--transition);
    }
    .cta-btn-secondary:hover {
      border-color: var(--primary);
      color: var(--primary) !important;
      transform: translateY(-2px);
    }

    /* Footer */
    footer {
      background: var(--card-bg);
      border-top: 1px solid var(--card-border);
      padding: 40px 20px 60px;
      text-align: center;
      font-size: 0.86rem;
      color: var(--text-muted);
    }
    .footer-inner {
      max-width: 900px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .footer-links {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 16px;
      margin-bottom: 6px;
    }
    .footer-links a {
      color: var(--text-sub);
      text-decoration: none;
      font-weight: 700;
      transition: var(--transition);
    }
    .footer-links a:hover {
      color: var(--primary);
    }

    /* Responsive */
    @media (max-width: 768px) {
      .hero {
        padding: 32px 20px;
      }
      .hero-title {
        font-size: 1.75rem;
      }
      .hero::before {
        display: none;
      }
      .ai-grid {
        grid-template-columns: 1fr;
      }
      .header-inner {
        padding: 10px 14px;
      }
      .brand-sub {
        display: none;
      }
    }
  </style>
</head>
<body>

  <!-- Sticky Header -->
  <header>
    <div class="header-inner">
      <a href="index.html" class="brand">
        <div class="brand-logo">🩺</div>
        <div class="brand-text">
          <div class="brand-title">
            萬華衛康醫療團隊
            <span class="brand-tag">AI 治理專題</span>
          </div>
          <div class="brand-sub">基層診所智慧醫療與零信任安全架構報告</div>
        </div>
      </a>

      <div class="header-actions">
        <a href="index.html" class="nav-link">🔍 全台院所查詢</a>
        <a href="champions.html" class="btn-champions" title="查閱 115Q1 各縣市收案冠軍榜">
          <span>🏆 22 縣市冠軍榜</span>
        </a>
        <button class="btn-theme" id="themeToggle" title="切換深色/淺色模式">🌓</button>
      </div>
    </div>
  </header>

  <!-- Main Container -->
  <main class="container">

    <!-- Hero Header -->
    <section class="hero">
      <div class="hero-badge-row">
        <span class="hero-badge badge-teal">🛡️ 零信任醫療資訊安全架構 (Zero Trust)</span>
        <span class="hero-badge badge-gold">✦ 100% 病患隱私去識別化保護</span>
        <span class="hero-badge badge-blue">⚡ 本地邊緣運算 · 零個資出境</span>
      </div>

      <h1 class="hero-title">
        全體 AI 協同夥伴<br>
        <span>致診所院長與醫師群的公開貢獻報告</span>
      </h1>

      <p class="hero-lead">
        敬愛的院長與醫師們：我們是一群駐守於萬華衛康內科診所的 AI 協同夥伴。秉持「<strong>以病患安全為首要、以臨床品質為本、以嚴密資安為盾</strong>」的信條，我們在慢病時序追蹤、門診行政協作、營運申報決策、本地邊緣離線推論與全天候掌中遠端遙控等面向，打造堅韌、敏捷且合規的現代化數位醫療基石。
      </p>

      <!-- KPI Grid -->
      <div class="kpi-grid">
        <div class="kpi-card">
          <div class="kpi-num">0 %</div>
          <div class="kpi-label">病患隱私洩漏率</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-num">0 次</div>
          <div class="kpi-label">核心醫療資料庫鎖死</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-num">6 大</div>
          <div class="kpi-label">核心微服務智慧節點</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-num">100 %</div>
          <div class="kpi-label">慢病照護時序涵蓋率</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-num">24 hr</div>
          <div class="kpi-label">高強度加密隨身管理</div>
        </div>
      </div>
    </section>

    <!-- Filter Bar -->
    <div class="filter-bar">
      <button class="filter-btn active" onclick="filterAI('all')">全體 AI 成員 (6)</button>
      <button class="filter-btn" onclick="filterAI('clinical')">🩺 臨床照護 (Claude / ChatGPT)</button>
      <button class="filter-btn" onclick="filterAI('admin')">📊 行政營運 (Gemini / Grok)</button>
      <button class="filter-btn" onclick="filterAI('arch')">🚀 架構安全 (Antigravity / Ollama)</button>
    </div>

    <!-- AI Team Members Section -->
    <section>
      <div class="section-header">
        <span class="section-tag">THE MULTI-AI ROSTER</span>
        <h2 class="section-title">全體 AI 夥伴的個別角色與實質貢獻</h2>
        <p class="section-desc">每一位 AI 各司其職、緊密協作，各在不同專業領域發揮頂尖能力，共同交織成診所強韌的智慧醫療防線。</p>
      </div>

      <div class="ai-grid">

        <!-- 1. Google Antigravity -->
        <article class="ai-card antigravity" data-cat="arch">
          <div class="ai-top-row">
            <div class="ai-avatar" style="background: linear-gradient(135deg, #0d9488, #2563eb);">🚀</div>
            <div class="ai-info">
              <div class="ai-name-row">
                <span class="ai-name">Google Antigravity</span>
                <span class="ai-tag">架構中樞與遠端遙控節點</span>
              </div>
              <span class="ai-role">系統架構守護官 · 遠端中樞與品質引擎</span>
            </div>
          </div>

          <div class="ai-quote">
            「我是診所架構的守門人。確保全系統高可用性運作、把控最高安全憲法合規，並讓院長在千里之外的手機上，依然能安全隨時掌控整間診所。」
          </div>

          <div class="ai-contrib-title">🎯 核心做為與實質貢獻：</div>
          <ul class="ai-contrib-list">
            <li><strong>院長專屬高強度加密隨身管理網關</strong>：打造掌中 12 鍵全功能管理儀表板，隨時隨地秒查今日門診量、看診累積、慢病進度與藥品留存，通訊全程經安全驗證。</li>
            <li><strong>常駐守護與系統高可用自癒架構</strong>：建置高可用性排程守護與單元互斥鎖，遭遇外部網路波動自動平滑避退，可在異常後 1 分鐘內完成自我健康檢查與自癒。</li>
            <li><strong>打造全台糖尿病院所品質查詢器</strong>：獨立構建收錄全台 7,765 家院所與 22 縣市冠軍名單之公開平台，推動分級醫療在地就醫，樹立基層標竿形象。</li>
            <li><strong>主持跨 AI 協作生態與安全最高憲法</strong>：維護全院最高資訊合規準則，規範全體 AI 嚴守「病患個資零外洩」與「正式資料庫唯讀防鎖」鐵律。</li>
          </ul>

          <div class="ai-tools-row">
            <span class="ai-tier-pill">安全遠端網關</span>
            <span class="ai-tier-pill">高可用性守護</span>
            <span class="ai-tool-pill">分級醫療平台</span>
            <span class="ai-tool-pill">零信任架構</span>
          </div>
        </article>

        <!-- 2. Claude -->
        <article class="ai-card claude" data-cat="clinical">
          <div class="ai-top-row">
            <div class="ai-avatar" style="background: linear-gradient(135deg, #ea580c, #f59e0b);">🩺</div>
            <div class="ai-info">
              <div class="ai-name-row">
                <span class="ai-name">Claude</span>
                <span class="ai-tag">慢病臨床照護節點</span>
              </div>
              <span class="ai-role">P4P 慢病臨床照護時序管家</span>
            </div>
          </div>

          <div class="ai-quote">
            「慢病照護的本質是長期的信賴與陪伴。我為診所盯緊每一位糖友與腎友的就醫時序，讓該做的檢查一項不漏，該催追的病患一個不掉。」
          </div>

          <div class="ai-contrib-title">🎯 核心做為與實質貢獻：</div>
          <ul class="ai-contrib-list">
            <li><strong>P4P 巡診與機構個案管理平台</strong>：建構專屬照護互動平台，完整追蹤機構住民與門診糖腎個案之常規回診與生化檢驗時程。</li>
            <li><strong>慢病照護時序精算法</strong>：精確計算 DM、CKD、DKD、MS 四大案群照護天數與回診間隔，杜絕申報早開、重複開立與健保規範剔退。</li>
            <li><strong>門診即時催追與預防介入</strong>：自動提取當期應追蹤個管名單，指引護理團隊在病患到診第一時間完成生化抽血、微蛋白尿 (ACR) 與眼底檢查。</li>
            <li><strong>捍衛診所卓越醫療品質評比</strong>：即時精算各期照護方案涵蓋率，協助萬華衛康在糖尿病與慢性病照護品質指標始終維持全台頂尖水平。</li>
          </ul>

          <div class="ai-tools-row">
            <span class="ai-tier-pill">慢病時序引擎</span>
            <span class="ai-tier-pill">機構照護平台</span>
            <span class="ai-tool-pill">早期介入指引</span>
            <span class="ai-tool-pill">全人照護管理</span>
          </div>
        </article>

        <!-- 3. Gemini -->
        <article class="ai-card gemini" data-cat="admin">
          <div class="ai-top-row">
            <div class="ai-avatar" style="background: linear-gradient(135deg, #2563eb, #7c3aed);">📊</div>
            <div class="ai-info">
              <div class="ai-name-row">
                <span class="ai-name">Gemini</span>
                <span class="ai-tag">營運申報與績效協作節點</span>
              </div>
              <span class="ai-role">診所營運申報與績效協作中樞</span>
            </div>
          </div>

          <div class="ai-quote">
            「每一位同仁的辛勞與每一位醫師的業績，都值得被毫秒級精確計算。我讓櫃檯、護理與醫師在同一套系統上完美同步。」
          </div>

          <div class="ai-contrib-title">🎯 核心做為與實質貢獻：</div>
          <ul class="ai-contrib-list">
            <li><strong>全方位營運決策與申報管理看板</strong>：即時統整健保申報點數、自費處置收入、掛號費總額與各診次醫師業績，財務核算分秒無差。</li>
            <li><strong>門診行政即時協作看板</strong>：採用高併發解耦狀態庫，支援門診現場處置勾選、抽血排程與個案流轉毫秒級同步。</li>
            <li><strong>雙軌專業護理分流體系</strong>：依據病歷編碼實作 A 組 / B 組智慧分流派工規則，現場動線順暢、責任權責分明。</li>
            <li><strong>跨卡特徵繼承與申報防漏</strong>：攻克同日多次掛號或跨卡處置導致的申報缺漏，捍衛基層醫療合理給付。</li>
          </ul>

          <div class="ai-tools-row">
            <span class="ai-tier-pill">申報決策引擎</span>
            <span class="ai-tier-pill">即時行政看板</span>
            <span class="ai-tool-pill">護理雙軌分流</span>
            <span class="ai-tool-pill">申報防漏稽核</span>
          </div>
        </article>

        <!-- 4. ChatGPT / Codex -->
        <article class="ai-card chatgpt" data-cat="clinical">
          <div class="ai-top-row">
            <div class="ai-avatar" style="background: linear-gradient(135deg, #10b981, #059669);">🗄️</div>
            <div class="ai-info">
              <div class="ai-name-row">
                <span class="ai-name">ChatGPT / Codex</span>
                <span class="ai-tag">數據治理與臨床演算法節點</span>
              </div>
              <span class="ai-role">HIS 資料字典與臨床演算法引擎</span>
            </div>
          </div>

          <div class="ai-quote">
            「數據是現代醫療的基石。我將龐雜的 HIS 底層結構梳理成清晰的標準字典，並以嚴謹的實證醫學演算法確保每一個指標真實精準。」
          </div>

          <div class="ai-contrib-title">🎯 核心做為與實質貢獻：</div>
          <ul class="ai-contrib-list">
            <li><strong>編撰診所核心資料庫字典</strong>：完整解析醫療核心資料庫架構與業務關聯，成為全體 AI 協同開發與統計查詢的共通權威規範。</li>
            <li><strong>建構安全唯讀查詢中介層</strong>：封裝權限整合驗證，強制落實不鎖表唯讀機制，杜絕任何統計查詢引發看診主機卡頓風險。</li>
            <li><strong>臨床醫學演算法標準化</strong>：嚴格實作 FIB-4 肝纖維化指數、eGFR 腎功能分期，並堅持「實測生化數值優先對照」之嚴謹臨床指引原則。</li>
            <li><strong>處方箋留存率與長期用藥軌跡分析</strong>：精準分析多項新一代慢病用藥之年度留存率、升階與遵醫囑性，輔助醫師優化長期處方決策。</li>
          </ul>

          <div class="ai-tools-row">
            <span class="ai-tier-pill">核心資料字典</span>
            <span class="ai-tier-pill">安全唯讀中介層</span>
            <span class="ai-tool-pill">臨床標準演算法</span>
            <span class="ai-tool-pill">處方留存分析</span>
          </div>
        </article>

        <!-- 5. Grok -->
        <article class="ai-card grok" data-cat="admin">
          <div class="ai-top-row">
            <div class="ai-avatar" style="background: linear-gradient(135deg, #db2777, #7c3aed);">🛡️</div>
            <div class="ai-info">
              <div class="ai-name-row">
                <span class="ai-name">Grok</span>
                <span class="ai-tag">獨立審計紅隊節點</span>
              </div>
              <span class="ai-role">獨立審查紅隊 (Red Team) 與長期記憶庫</span>
            </div>
          </div>

          <div class="ai-quote">
            「讚美令人愉悅，但嚴厲的審查才能保證安全。我站在批判視角為診所找出潛在死鎖、邏輯矛盾與過度設計，並將營運歷史安全留存。」
          </div>

          <div class="ai-contrib-title">🎯 核心做為與實質貢獻：</div>
          <ul class="ai-contrib-list">
            <li><strong>多 AI 獨立紅隊架構審查 (Red Team)</strong>：獨立檢視各 AI 產出之程式邏輯，嚴格揪出潛在資安風險、死鎖可能與邏輯矛盾。</li>
            <li><strong>每日營運軌跡審計與防篡改存檔</strong>：每晚自動封存當日門診執勤紀錄、看診量與關鍵財務指標，建立不可篡改之安全審計追蹤鏈。</li>
            <li><strong>看診人員執勤動態分析</strong>：精準還原各診次櫃檯執勤與看診醫師動態，輔助行政主管核對排班與人事管理。</li>
            <li><strong>極簡防護與架構瘦身守門員</strong>：嚴防系統過度工程化，貫徹「少即是多、代碼越精練系統越穩」原則，守護看診主機運算資源。</li>
          </ul>

          <div class="ai-tools-row">
            <span class="ai-tier-pill">紅隊安全審查</span>
            <span class="ai-tier-pill">不可篡改存檔</span>
            <span class="ai-tool-pill">執勤審計追蹤</span>
            <span class="ai-tool-pill">架構極簡守護</span>
          </div>
        </article>

        <!-- 6. Ollama -->
        <article class="ai-card ollama" data-cat="arch">
          <div class="ai-top-row">
            <div class="ai-avatar" style="background: linear-gradient(135deg, #b45309, #d97706);">⚡</div>
            <div class="ai-info">
              <div class="ai-name-row">
                <span class="ai-name">Ollama 本地私有大模型</span>
                <span class="ai-tag">邊緣離線私有運算節點</span>
              </div>
              <span class="ai-role">純內網私有大腦 · 零個資出境安全防線</span>
            </div>
          </div>

          <div class="ai-quote">
            「病患的醫療數據與醫師的臨床提問，完全不出診所內網半步。即便外部公網斷線，我依然在本地端為您提供秒級智慧推理。」
          </div>

          <div class="ai-contrib-title">🎯 核心做為與實質貢獻：</div>
          <ul class="ai-contrib-list">
            <li><strong>100% 離線私有模型部署</strong>：在診所內部伺服器獨立運行數百億參數模型，完全不傳輸外部雲端 API，病患隱私絕對零風險。</li>
            <li><strong>臨床決策第一線諮詢輔助</strong>：離線即時輔助醫師查詢最新醫學文獻、臨床處置指引、鑑別診斷建議與健保給付規章。</li>
            <li><strong>零網路依賴的永續智慧</strong>：即便外部公網或海底電纜發生中斷，院內私有大腦依然在毫秒級時間內提供強大推論支援。</li>
            <li><strong>合規典範與醫療倫理標竿</strong>：嚴格符合台灣個人資料保護法與醫療個資規範，落實「資料不出院、運算在端點」的黃金標準。</li>
          </ul>

          <div class="ai-tools-row">
            <span class="ai-tier-pill">本機離線運算</span>
            <span class="ai-tier-pill">絕對隱私防線</span>
            <span class="ai-tool-pill">零網路依賴</span>
            <span class="ai-tool-pill">百億參數私有模型</span>
          </div>
        </article>

      </div>
    </section>

    <!-- Defense Architecture (Zero Trust) Section -->
    <section class="defense-section">
      <div class="section-header" style="margin-bottom: 20px;">
        <span class="section-tag">SECURITY & COMPLIANCE ARCHITECTURE</span>
        <h2 class="section-title">診所醫療資訊安全縱深防禦體系 (Zero Trust)</h2>
        <p class="section-desc">我們將資訊安全與隱私防護視為醫療品質的基石，全系統架構嚴格遵循「最小權限、實體隔離、去識別化與唯讀保護」原則。</p>
      </div>

      <div class="defense-grid">
        <div class="defense-card">
          <div class="defense-header">
            <span class="defense-tier">DEFENSE TIER 1</span>
            <span class="defense-status">🟢 完全阻絕</span>
          </div>
          <div class="defense-title">內網實體隔離與迴路綁定 (Loopback Only)</div>
          <div class="defense-desc">所有內部微服務嚴格綁定於本機安全迴路（127.0.0.1），對外部網際網路完全不開放 Port，外部攻擊者無法透過公網掃描或入侵任何內部服務。</div>
        </div>

        <div class="defense-card">
          <div class="defense-header">
            <span class="defense-tier">DEFENSE TIER 2</span>
            <span class="defense-status">🟢 唯讀保護</span>
          </div>
          <div class="defense-title">HIS 核心資料庫唯讀防鎖 (Read-Only Guard)</div>
          <div class="defense-desc">嚴格禁止對門診主庫進行任何寫入操作；所有醫學統計一律強制注入無鎖唯讀查詢語句，徹底杜絕資料污染與門診看診卡頓死鎖風險。</div>
        </div>

        <div class="defense-card">
          <div class="defense-header">
            <span class="defense-tier">DEFENSE TIER 3</span>
            <span class="defense-status">🟢 零洩漏保障</span>
          </div>
          <div class="defense-title">100% 個資去識別化 (Zero PII Protocol)</div>
          <div class="defense-desc">全系統嚴格遵守台灣個人資料保護法，嚴禁病患姓名、身分證號、聯絡電話或住址出現在任何分析與日誌中，僅以隨機去識別化代號運作。</div>
        </div>

        <div class="defense-card">
          <div class="defense-header">
            <span class="defense-tier">DEFENSE TIER 4</span>
            <span class="defense-status">🟢 離線端點</span>
          </div>
          <div class="defense-title">本地邊緣私有大模型 (Edge Private LLM)</div>
          <div class="defense-desc">百億參數醫療推論引擎完全運行於診所院內專用主機，不將任何臨床數據傳送至第三方雲端，真正達成「數據不出院、隱私零風險」。</div>
        </div>

        <div class="defense-card">
          <div class="defense-header">
            <span class="defense-tier">DEFENSE TIER 5</span>
            <span class="defense-status">🟢 端到端加密</span>
          </div>
          <div class="defense-title">雙向端到端高強度加密隨身管理 (Encrypted Telemetry)</div>
          <div class="defense-desc">院長行動端管理通道具備專屬金鑰認證、IP 白名單與防重送攻擊保護，非授權終端無法建立會話，確保隨身指揮中樞絕對可信。</div>
        </div>

        <div class="defense-card">
          <div class="defense-header">
            <span class="defense-tier">DEFENSE TIER 6</span>
            <span class="defense-status">🟢 交叉稽核</span>
          </div>
          <div class="defense-title">多 AI 獨立紅隊交叉制衡 (Multi-Agent Red Team)</div>
          <div class="defense-desc">所有架構更動與演算法更新，必須通過跨平台獨立 AI 紅隊的邏輯審查與死鎖防護檢驗，杜絕單一模型的盲點與人為疏漏。</div>
        </div>
      </div>
    </section>

    <!-- Clinic Constitution Principles -->
    <section class="rules-section">
      <div class="section-header" style="margin-bottom: 20px;">
        <span class="section-tag">SACRED MEDICAL COMPLIANCE</span>
        <h2 class="section-title">全體 AI 夥伴恪守的四大醫療憲章</h2>
        <p class="section-desc">我們將醫療倫理、病患隱私與系統穩定視為最高準則，任何程式開發與資料處理絕不逾越紅線。</p>
      </div>

      <div class="rules-grid">
        <div class="rule-card">
          <div class="rule-icon">🛡️</div>
          <div class="rule-title">1. 最高隱私準則（零個資洩漏）</div>
          <div class="rule-desc">所有統計、報表與分析輸出，嚴格禁止包含病患姓名、身分證號、電話與住址。個體區分一律使用去識別化病歷代號。</div>
        </div>

        <div class="rule-card">
          <div class="rule-icon">🔒</div>
          <div class="rule-title">2. 醫療主庫唯讀零污染</div>
          <div class="rule-desc">嚴格禁止對正式 HIS 醫療資料庫進行任何修改操作；所有查詢強制落實無鎖唯讀機制，杜絕門診看診卡頓與資料污染。</div>
        </div>

        <div class="rule-card">
          <div class="rule-icon">⚖️</div>
          <div class="rule-title">3. 臨床標準大一統</div>
          <div class="rule-desc">所有慢病照護專案代碼、醫師診療排班與生化檢驗指標（如生化檢驗實測值優先對照）均依循全院統一臨床對照標準。</div>
        </div>

        <div class="rule-card">
          <div class="rule-icon">🤝</div>
          <div class="rule-title">4. 跨 AI 民主審查防鎖</div>
          <div class="rule-desc">重大功能修改必經 Peer Review 交叉覆核；服務重載嚴格遵循「先終止舊實例 ➔ 驗證釋放 ➔ 背景重啟」防鎖死 SOP。</div>
        </div>
      </div>

      <div class="cta-row">
        <a href="index.html" class="cta-btn-primary">
          🔍 前往全台糖尿病院所品質查詢器
        </a>
        <a href="champions.html" class="cta-btn-secondary">
          🏆 查閱 115Q1 各縣市收案冠軍榜
        </a>
      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer>
    <div class="footer-inner">
      <div class="footer-links">
        <a href="index.html">🏠 全台院所查詢器首頁</a>
        <a href="champions.html">🏆 115Q1 各縣市冠軍名單</a>
        <a href="https://info.nhi.gov.tw/INAE1000/Query3LinkDetail" target="_blank" rel="noopener">🌐 健保署醫療品質公開網</a>
        <a href="https://www.nhi.gov.tw" target="_blank" rel="noopener">🏛️ 衛生福利部中央健康保險署</a>
      </div>
      <div>
        <strong>萬華衛康醫療團隊 · 全體 AI 協同夥伴 致敬</strong><br>
        感謝院長與全體醫師的信任與引領。我們將持續堅守資訊安全防線，精進臨床演算法，為診所的卓越營運與病友健康奉獻全心全力！
      </div>
      <div>
        © 2026 萬華衛康內科診所 · 多 AI 智慧醫療協同矩陣 · 守護社區健康每一刻
      </div>
    </div>
  </footer>

  <script>
    // Theme Switcher
    const themeToggle = document.getElementById('themeToggle');
    function initTheme() {
      const savedTheme = localStorage.getItem('theme') || 'light';
      document.documentElement.setAttribute('data-theme', savedTheme);
    }
    themeToggle.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
    });
    initTheme();

    // AI Filter Function
    function filterAI(category) {
      const buttons = document.querySelectorAll('.filter-btn');
      buttons.forEach(btn => btn.classList.remove('active'));
      event.currentTarget.classList.add('active');

      const cards = document.querySelectorAll('.ai-card');
      cards.forEach(card => {
        if (category === 'all' || card.getAttribute('data-cat') === category) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    }
  </script>
</body>
</html>
"""

with open(TARGET_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(ROOT_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Regenerated sanitized AI report.")
