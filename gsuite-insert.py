#!/usr/bin/env python3
"""Insert Google Suite interactive demo into the portfolio."""

import re

CSS_BLOCK = r"""
/* ============================================
   GOOGLE SUITE DASHBOARD
   ============================================ */
.gsuite-demo {
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-md);
  transition: background-color 0.4s var(--ease-out), border-color 0.4s var(--ease-out);
}

/* ---- Google Suite Header ---- */
.gsuite-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 16px;
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--color-text);
  border-bottom: 1px solid var(--color-border);
  background: var(--color-bg-card);
  transition: background-color 0.4s var(--ease-out), border-color 0.4s var(--ease-out);
}

.gsuite-header-dots {
  display: flex;
  gap: 4px;
}

.gsuite-header-dots span {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  display: block;
}

.gsuite-header-dots span:nth-child(1) { background: #4285F4; }
.gsuite-header-dots span:nth-child(2) { background: #EA4335; }
.gsuite-header-dots span:nth-child(3) { background: #FBBC05; }
.gsuite-header-dots span:nth-child(4) { background: #34A853; }

/* ---- Google Suite Tabs ---- */
.gsuite-tabs {
  display: flex;
  border-bottom: 1px solid var(--color-border);
  background: var(--color-bg-card);
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  transition: background-color 0.4s var(--ease-out), border-color 0.4s var(--ease-out);
}

.gsuite-tab {
  padding: var(--space-3) var(--space-5);
  font-size: 0.82rem;
  font-weight: 500;
  color: var(--color-text-muted);
  background: none;
  border: none;
  cursor: pointer;
  position: relative;
  white-space: nowrap;
  transition: color 0.2s;
}

.gsuite-tab:hover {
  color: var(--color-text);
}

.gsuite-tab.active {
  color: #4285F4;
  font-weight: 600;
}

.gsuite-tab.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: #4285F4;
  border-radius: 3px 3px 0 0;
}

[data-theme="dark"] .gsuite-tab.active {
  color: #8AB4F8;
}

[data-theme="dark"] .gsuite-tab.active::after {
  background: #8AB4F8;
}

/* ---- Google Suite Panel ---- */
.gsuite-panel {
  display: none;
  padding: 0;
}

.gsuite-panel.active {
  display: block;
}

/* ---- Gmail Tab ---- */
.gsuite-gmail-bar {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 16px;
  border-bottom: 1px solid var(--color-border);
}

.gsuite-compose-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 20px;
  background: #4285F4;
  color: #fff;
  border: none;
  border-radius: 24px;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: default;
  white-space: nowrap;
  box-shadow: 0 1px 3px rgba(66,133,244,0.3);
  flex-shrink: 0;
}

[data-theme="dark"] .gsuite-compose-btn {
  background: #8AB4F8;
  color: #1a1a2e;
}

.gsuite-gmail-search {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: 8px;
  padding: 6px 12px;
  transition: border-color 0.2s, background-color 0.4s var(--ease-out);
}

.gsuite-gmail-search svg {
  opacity: 0.5;
  flex-shrink: 0;
}

.gsuite-gmail-search input {
  flex: 1;
  border: none;
  background: none;
  font-size: 0.8rem;
  color: var(--color-text);
  outline: none;
  min-width: 0;
}

.gsuite-gmail-search input::placeholder {
  color: var(--color-text-muted);
}

.gsuite-email-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.gsuite-email-row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 16px;
  border-bottom: 1px solid var(--color-border-light, var(--color-border));
  cursor: pointer;
  transition: background-color 0.15s;
}

.gsuite-email-row:hover {
  background: rgba(66,133,244,0.04);
}

[data-theme="dark"] .gsuite-email-row:hover {
  background: rgba(138,180,248,0.06);
}

.gsuite-email-row.unread .gsuite-email-sender,
.gsuite-email-row.unread .gsuite-email-subject {
  font-weight: 700;
}

.gsuite-email-row.unread .gsuite-email-dot {
  display: block;
}

.gsuite-email-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 600;
  color: #fff;
  flex-shrink: 0;
}

.gsuite-email-content {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.gsuite-email-top {
  display: flex;
  align-items: center;
  gap: 8px;
}

.gsuite-email-sender {
  font-size: 0.82rem;
  font-weight: 500;
  color: var(--color-text);
  white-space: nowrap;
}

.gsuite-email-dot {
  display: none;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #4285F4;
  flex-shrink: 0;
}

[data-theme="dark"] .gsuite-email-dot {
  background: #8AB4F8;
}

.gsuite-email-subject {
  font-size: 0.8rem;
  color: var(--color-text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.gsuite-email-preview {
  font-size: 0.78rem;
  color: var(--color-text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.gsuite-email-date {
  font-size: 0.75rem;
  color: var(--color-text-muted);
  white-space: nowrap;
  flex-shrink: 0;
}

.gsuite-email-row.unread .gsuite-email-date {
  color: var(--color-text);
  font-weight: 600;
}

/* Email expanded */
.gsuite-email-expanded {
  display: none;
  padding: 12px 16px 12px 64px;
  font-size: 0.8rem;
  line-height: 1.6;
  color: var(--color-text-secondary);
  border-bottom: 1px solid var(--color-border-light, var(--color-border));
  background: rgba(66,133,244,0.02);
}

[data-theme="dark"] .gsuite-email-expanded {
  background: rgba(138,180,248,0.03);
}

.gsuite-email-expanded.visible {
  display: block;
}

/* ---- Sheets Tab ---- */
.gsuite-sheets-bar {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 12px;
  background: #34A853;
  color: #fff;
  font-size: 0.8rem;
  font-weight: 600;
}

[data-theme="dark"] .gsuite-sheets-bar {
  background: #1e6e35;
}

.gsuite-sheets-bar svg {
  flex-shrink: 0;
}

.gsuite-formula-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 12px;
  border-bottom: 1px solid var(--color-border);
  font-size: 0.78rem;
  color: var(--color-text-muted);
  background: var(--color-bg-card);
}

.gsuite-formula-bar span {
  padding: 2px 8px;
  border: 1px solid var(--color-border);
  border-radius: 4px;
  font-weight: 600;
  font-size: 0.72rem;
  color: var(--color-text);
  background: var(--color-bg);
}

.gsuite-formula-bar code {
  flex: 1;
  font-family: 'SF Mono', 'Fira Code', monospace;
  font-size: 0.75rem;
  color: var(--color-text);
}

.gsuite-sheet-wrap {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.gsuite-sheet {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.78rem;
  min-width: 580px;
}

.gsuite-sheet th {
  background: var(--color-bg);
  color: var(--color-text-muted);
  font-weight: 500;
  font-size: 0.72rem;
  padding: 6px 10px;
  border: 1px solid var(--color-border);
  text-align: center;
  position: sticky;
  top: 0;
}

.gsuite-sheet td {
  padding: 7px 10px;
  border: 1px solid var(--color-border-light, var(--color-border));
  color: var(--color-text);
  white-space: nowrap;
}

.gsuite-sheet .gsuite-row-num {
  background: var(--color-bg);
  color: var(--color-text-muted);
  text-align: center;
  font-size: 0.72rem;
  width: 36px;
  font-weight: 500;
}

.gsuite-sheet .gsuite-cell-selected {
  outline: 2px solid #4285F4;
  outline-offset: -1px;
  background: rgba(66,133,244,0.06);
}

[data-theme="dark"] .gsuite-sheet .gsuite-cell-selected {
  outline-color: #8AB4F8;
  background: rgba(138,180,248,0.08);
}

/* ---- Drive Tab ---- */
.gsuite-drive-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  font-size: 0.8rem;
  color: var(--color-text-muted);
  border-bottom: 1px solid var(--color-border);
}

.gsuite-drive-bar a,
.gsuite-breadcrumb {
  color: var(--color-text-muted);
  text-decoration: none;
  font-size: 0.8rem;
}

.gsuite-breadcrumb-current {
  color: var(--color-text);
  font-weight: 600;
}

.gsuite-drive-grid {
  padding: 12px 16px;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.gsuite-drive-section-label {
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 8px 0 6px;
}

.gsuite-drive-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 10px;
  border-radius: 8px;
  transition: background-color 0.15s;
  cursor: default;
}

.gsuite-drive-item:hover {
  background: rgba(66,133,244,0.04);
}

[data-theme="dark"] .gsuite-drive-item:hover {
  background: rgba(138,180,248,0.06);
}

.gsuite-drive-icon {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.gsuite-drive-icon svg {
  width: 22px;
  height: 22px;
}

.gsuite-drive-name {
  flex: 1;
  font-size: 0.82rem;
  color: var(--color-text);
}

.gsuite-drive-meta {
  font-size: 0.72rem;
  color: var(--color-text-muted);
  white-space: nowrap;
}

/* ---- Calendar Tab ---- */
.gsuite-cal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 16px;
  border-bottom: 1px solid var(--color-border);
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--color-text);
}

.gsuite-cal-header span {
  color: var(--color-text-muted);
  font-weight: 400;
  font-size: 0.78rem;
}

.gsuite-cal-wrap {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.gsuite-cal-grid {
  display: grid;
  grid-template-columns: 54px repeat(5, 1fr);
  min-width: 560px;
}

.gsuite-cal-day-header {
  padding: 8px 4px;
  text-align: center;
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  border-bottom: 1px solid var(--color-border);
  border-right: 1px solid var(--color-border-light, var(--color-border));
}

.gsuite-cal-day-header:last-child {
  border-right: none;
}

.gsuite-cal-time {
  padding: 0 6px;
  font-size: 0.68rem;
  color: var(--color-text-muted);
  text-align: right;
  border-right: 1px solid var(--color-border);
  height: 52px;
  display: flex;
  align-items: flex-start;
  justify-content: flex-end;
  padding-top: 2px;
}

.gsuite-cal-corner {
  border-bottom: 1px solid var(--color-border);
  border-right: 1px solid var(--color-border);
}

.gsuite-cal-cell {
  border-bottom: 1px solid var(--color-border-light, var(--color-border));
  border-right: 1px solid var(--color-border-light, var(--color-border));
  height: 52px;
  position: relative;
  padding: 2px;
}

.gsuite-cal-cell:nth-child(6n+1) {
  /* time column handled separately */
}

.gsuite-cal-cell:last-child {
  border-right: none;
}

.gsuite-cal-event {
  padding: 3px 6px;
  border-radius: 4px;
  font-size: 0.68rem;
  font-weight: 600;
  color: #fff;
  line-height: 1.3;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  height: 100%;
  display: flex;
  align-items: center;
}

.gsuite-cal-event--blue { background: #4285F4; }
.gsuite-cal-event--green { background: #34A853; }
.gsuite-cal-event--purple { background: #8E24AA; }
.gsuite-cal-event--red { background: #EA4335; }

[data-theme="dark"] .gsuite-cal-event--blue { background: #3b6fcf; }
[data-theme="dark"] .gsuite-cal-event--green { background: #2a8a45; }
[data-theme="dark"] .gsuite-cal-event--purple { background: #7a1fa0; }
[data-theme="dark"] .gsuite-cal-event--red { background: #c5362b; }

/* ---- Google Suite Responsive ---- */
@media (max-width: 640px) {
  .gsuite-tab {
    padding: var(--space-2) var(--space-4);
    font-size: 0.78rem;
  }

  .gsuite-gmail-bar {
    flex-direction: column;
    align-items: stretch;
    gap: 8px;
  }

  .gsuite-compose-btn {
    align-self: flex-start;
  }

  .gsuite-email-row {
    padding: 8px 12px;
    gap: 8px;
  }

  .gsuite-email-avatar {
    width: 30px;
    height: 30px;
    font-size: 0.65rem;
  }

  .gsuite-email-expanded {
    padding-left: 50px;
  }

  .gsuite-drive-grid {
    padding: 8px 12px;
  }
}
"""

HTML_BLOCK = r"""
<!-- Google Suite -->
        <div class="section__header reveal" style="margin-top: clamp(var(--space-16), 8vw, var(--space-32));">
          <h2 class="section__title">Google Suite</h2>
          <p class="volunteer-card__duration" style="margin-top: var(--space-3);">Utilized at Red Clay CPAs LLC</p>
          <p class="analytics__intro" style="margin-top: var(--space-6);">Managed client communications, scheduling, document storage, and collaborative reporting using Google Workspace. Coordinated scheduling and actionable insights for client needs across Gmail, Sheets, Drive, and Calendar. These numbers draw from real examples, but are fabricated to showcase the functionality of my skill set in Google Suite.</p>
        </div>
        <div class="gsuite-demo reveal">
          <!-- Header -->
          <div class="gsuite-header">
            <div class="gsuite-header-dots"><span></span><span></span><span></span><span></span></div>
            Google Suite &mdash; Red Clay CPAs
          </div>
          <!-- Tabs -->
          <div class="gsuite-tabs">
            <button class="gsuite-tab active" data-gsuite-tab="gmail">Gmail</button>
            <button class="gsuite-tab" data-gsuite-tab="sheets">Sheets</button>
            <button class="gsuite-tab" data-gsuite-tab="drive">Drive</button>
            <button class="gsuite-tab" data-gsuite-tab="calendar">Calendar</button>
          </div>
          <!-- Gmail Panel -->
          <div class="gsuite-panel active" id="gsuiteGmail">
            <div class="gsuite-gmail-bar">
              <button class="gsuite-compose-btn"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>Compose</button>
              <div class="gsuite-gmail-search">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                <input type="text" placeholder="Search mail..." readonly>
              </div>
            </div>
            <ul class="gsuite-email-list" id="gsuiteEmailList">
              <!-- Populated by JS -->
            </ul>
          </div>
          <!-- Sheets Panel -->
          <div class="gsuite-panel" id="gsuiteSheets">
            <div class="gsuite-sheets-bar">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="9" y1="3" x2="9" y2="21"/></svg>
              Client Tracking &mdash; Red Clay CPAs
            </div>
            <div class="gsuite-formula-bar">
              <span>D2</span>
              <code>=TEXT(DATE(2024,4,15),"MMM DD, YYYY")</code>
            </div>
            <div class="gsuite-sheet-wrap">
              <table class="gsuite-sheet" id="gsuiteSheetTable">
                <!-- Populated by JS -->
              </table>
            </div>
          </div>
          <!-- Drive Panel -->
          <div class="gsuite-panel" id="gsuiteDrive">
            <div class="gsuite-drive-bar">
              <span class="gsuite-breadcrumb">My Drive</span>
              <span style="color:var(--color-text-muted);">&rsaquo;</span>
              <span class="gsuite-breadcrumb-current">Red Clay CPAs</span>
            </div>
            <div class="gsuite-drive-grid" id="gsuiteDriveGrid">
              <!-- Populated by JS -->
            </div>
          </div>
          <!-- Calendar Panel -->
          <div class="gsuite-panel" id="gsuiteCalendar">
            <div class="gsuite-cal-header">
              <div>March 2024</div>
              <span>Week View</span>
            </div>
            <div class="gsuite-cal-wrap">
              <div class="gsuite-cal-grid" id="gsuiteCalGrid">
                <!-- Populated by JS -->
              </div>
            </div>
          </div>
        </div>
"""

JS_BLOCK = r"""
  <script>
  /* ============================================
     GOOGLE SUITE DASHBOARD
     ============================================ */
  (function() {
    // ---- Tab switching ----
    var gsuiteTabs = document.querySelectorAll('[data-gsuite-tab]');
    for (var t = 0; t < gsuiteTabs.length; t++) {
      gsuiteTabs[t].addEventListener('click', (function(tab) {
        return function() {
          var view = tab.getAttribute('data-gsuite-tab');
          for (var i = 0; i < gsuiteTabs.length; i++) {
            gsuiteTabs[i].classList.remove('active');
          }
          tab.classList.add('active');
          var panels = document.querySelectorAll('.gsuite-panel');
          for (var i = 0; i < panels.length; i++) {
            panels[i].classList.remove('active');
          }
          var target = document.getElementById('gsuite' + view.charAt(0).toUpperCase() + view.slice(1));
          if (target) target.classList.add('active');
        };
      })(gsuiteTabs[t]));
    }

    // ---- Gmail ----
    var emails = [
      { from: "Sarah Johnson", subject: "Tax Documents Uploaded", preview: "Hi Jack, I've uploaded all the W-2s and 1099s to the shared Drive folder...", date: "Mar 12", unread: true, color: "#4285F4" },
      { from: "Mike Thompson", subject: "RE: Q1 Estimated Tax Payment", preview: "Thanks for the reminder. I'll have the payment sent by Friday...", date: "Mar 11", unread: true, color: "#EA4335" },
      { from: "Jennifer Davis", subject: "Meeting Rescheduled", preview: "Can we move our Thursday review to 2pm instead? I have a conflict...", date: "Mar 10", unread: false, color: "#34A853" },
      { from: "Red Clay CPAs Team", subject: "Monthly Client Report - February", preview: "Attached is the February client engagement report for review...", date: "Mar 8", unread: false, color: "#FBBC05" },
      { from: "David Chen", subject: "Extension Filing Request", preview: "I need to file an extension for my business return. Can you help...", date: "Mar 7", unread: true, color: "#8E24AA" },
      { from: "Lisa Martinez", subject: "Invoice Question", preview: "I received the invoice for Q4 services but have a question about...", date: "Mar 5", unread: false, color: "#EA4335" },
      { from: "Robert Kim", subject: "New Client Onboarding", preview: "Please find the signed engagement letter and organizer attached...", date: "Mar 3", unread: false, color: "#4285F4" },
      { from: "Amy Wilson", subject: "Payroll Processing Complete", preview: "February payroll has been processed. All direct deposits confirmed...", date: "Mar 1", unread: false, color: "#34A853" }
    ];

    var emailList = document.getElementById('gsuiteEmailList');
    if (emailList) {
      var html = '';
      for (var i = 0; i < emails.length; i++) {
        var e = emails[i];
        var initials = e.from.split(' ').map(function(w) { return w[0]; }).join('').substring(0, 2);
        html += '<li>';
        html += '<div class="gsuite-email-row' + (e.unread ? ' unread' : '') + '" data-email-idx="' + i + '">';
        html += '<div class="gsuite-email-avatar" style="background:' + e.color + ';">' + initials + '</div>';
        html += '<div class="gsuite-email-content">';
        html += '<div class="gsuite-email-top"><span class="gsuite-email-sender">' + e.from + '</span><span class="gsuite-email-dot"></span></div>';
        html += '<div class="gsuite-email-subject">' + e.subject + '</div>';
        html += '<div class="gsuite-email-preview">' + e.preview + '</div>';
        html += '</div>';
        html += '<div class="gsuite-email-date">' + e.date + '</div>';
        html += '</div>';
        html += '<div class="gsuite-email-expanded" data-email-expand="' + i + '">';
        html += '<strong>From:</strong> ' + e.from + '<br>';
        html += '<strong>Subject:</strong> ' + e.subject + '<br><br>';
        html += e.preview;
        html += '</div>';
        html += '</li>';
      }
      emailList.innerHTML = html;

      // Click to toggle expand
      var rows = emailList.querySelectorAll('.gsuite-email-row');
      for (var r = 0; r < rows.length; r++) {
        rows[r].addEventListener('click', (function(row) {
          return function() {
            var idx = row.getAttribute('data-email-idx');
            var expand = document.querySelector('[data-email-expand="' + idx + '"]');
            if (expand) {
              expand.classList.toggle('visible');
            }
          };
        })(rows[r]));
      }
    }

    // ---- Sheets ----
    var sheetData = [
      ["Johnson, Sarah", "Tax Return - 1040", "In Progress", "Apr 15, 2024", "W-2s received"],
      ["Thompson, Mike", "Estimated Taxes", "Awaiting Client", "Apr 15, 2024", "Q1 payment pending"],
      ["Davis, Jennifer", "Tax Return - 1040", "In Progress", "Apr 15, 2024", "Review scheduled Thu"],
      ["Chen, David", "Business Tax - 1120S", "Extension Filed", "Oct 15, 2024", "Extension approved"],
      ["Martinez, Lisa", "Bookkeeping", "Completed", "Mar 31, 2024", "Q4 reconciled"],
      ["Kim, Robert", "New Client Onboard", "New Intake", "Apr 1, 2024", "Engagement letter signed"],
      ["Wilson, Amy", "Payroll Processing", "Completed", "Feb 28, 2024", "Feb payroll confirmed"],
      ["Blue Ridge Contracting", "Business Tax - 1065", "In Progress", "Mar 15, 2024", "K-1s pending"]
    ];
    var sheetHeaders = ["", "A", "B", "C", "D", "E"];
    var colHeaders = ["", "Client Name", "Service", "Status", "Due Date", "Notes"];

    var sheetTable = document.getElementById('gsuiteSheetTable');
    if (sheetTable) {
      var html = '<thead><tr>';
      for (var h = 0; h < sheetHeaders.length; h++) {
        html += '<th>' + sheetHeaders[h] + '</th>';
      }
      html += '</tr></thead><tbody>';
      // Column header row
      html += '<tr>';
      html += '<td class="gsuite-row-num">1</td>';
      for (var c = 1; c < colHeaders.length; c++) {
        html += '<td style="font-weight:600;background:var(--color-bg);">' + colHeaders[c] + '</td>';
      }
      html += '</tr>';
      for (var r = 0; r < sheetData.length; r++) {
        html += '<tr>';
        html += '<td class="gsuite-row-num">' + (r + 2) + '</td>';
        for (var c = 0; c < sheetData[r].length; c++) {
          var cls = (r === 0 && c === 3) ? ' class="gsuite-cell-selected"' : '';
          html += '<td' + cls + '>' + sheetData[r][c] + '</td>';
        }
        html += '</tr>';
      }
      html += '</tbody>';
      sheetTable.innerHTML = html;
    }

    // ---- Drive ----
    var driveItems = [
      { type: "folder", name: "2024 Tax Returns", meta: "24 files", color: "#FBBC05" },
      { type: "folder", name: "Client Documents", meta: "18 files", color: "#FBBC05" },
      { type: "folder", name: "Templates", meta: "6 files", color: "#FBBC05" },
      { type: "folder", name: "Reports", meta: "12 files", color: "#FBBC05" },
      { type: "xlsx", name: "Q1 Revenue Report.xlsx", meta: "Mar 5, 2024", color: "#34A853" },
      { type: "docx", name: "Client Onboarding Checklist.docx", meta: "Feb 20, 2024", color: "#4285F4" },
      { type: "pdf", name: "Engagement Letter Template.pdf", meta: "Jan 10, 2024", color: "#EA4335" }
    ];

    var folderIcon = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M10 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2z"/></svg>';
    var sheetIcon = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V8l-6-6zm-1 7V3.5L18.5 9H13zM8 13h8v2H8v-2zm0 4h5v2H8v-2z"/></svg>';
    var docIcon = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V8l-6-6zm-1 7V3.5L18.5 9H13zM8 13h8v2H8v-2zm0 4h8v2H8v-2z"/></svg>';
    var pdfIcon = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V8l-6-6zm-1 7V3.5L18.5 9H13zM8 17h2v-4h1.5c.83 0 1.5-.67 1.5-1.5S12.33 10 11.5 10H8v7z"/></svg>';

    function getDriveIcon(type) {
      if (type === 'folder') return folderIcon;
      if (type === 'xlsx') return sheetIcon;
      if (type === 'docx') return docIcon;
      if (type === 'pdf') return pdfIcon;
      return docIcon;
    }

    var driveGrid = document.getElementById('gsuiteDriveGrid');
    if (driveGrid) {
      var html = '<div class="gsuite-drive-section-label">Folders</div>';
      for (var i = 0; i < driveItems.length; i++) {
        var d = driveItems[i];
        if (d.type === 'folder') {
          html += '<div class="gsuite-drive-item">';
          html += '<div class="gsuite-drive-icon" style="color:' + d.color + ';">' + getDriveIcon(d.type) + '</div>';
          html += '<div class="gsuite-drive-name">' + d.name + '</div>';
          html += '<div class="gsuite-drive-meta">' + d.meta + '</div>';
          html += '</div>';
        }
      }
      html += '<div class="gsuite-drive-section-label" style="margin-top:4px;">Files</div>';
      for (var i = 0; i < driveItems.length; i++) {
        var d = driveItems[i];
        if (d.type !== 'folder') {
          html += '<div class="gsuite-drive-item">';
          html += '<div class="gsuite-drive-icon" style="color:' + d.color + ';">' + getDriveIcon(d.type) + '</div>';
          html += '<div class="gsuite-drive-name">' + d.name + '</div>';
          html += '<div class="gsuite-drive-meta">' + d.meta + '</div>';
          html += '</div>';
        }
      }
      driveGrid.innerHTML = html;
    }

    // ---- Calendar ----
    var days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'];
    var times = ['9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM'];
    // Events keyed by "day-time"
    var calEvents = {
      '0-0': { text: 'Team Standup', cls: 'blue' },
      '0-5': { text: 'Johnson Tax Review', cls: 'green' },
      '1-1': { text: 'Client Onboarding - Kim', cls: 'purple' },
      '2-2': { text: 'Q1 Deadline Prep', cls: 'red' },
      '3-5': { text: 'Davis Account Review', cls: 'green' },
      '4-0': { text: 'Weekly Report', cls: 'blue' }
    };

    var calGrid = document.getElementById('gsuiteCalGrid');
    if (calGrid) {
      var html = '<div class="gsuite-cal-corner"></div>';
      for (var d = 0; d < days.length; d++) {
        html += '<div class="gsuite-cal-day-header">' + days[d] + '</div>';
      }
      for (var t = 0; t < times.length; t++) {
        html += '<div class="gsuite-cal-time">' + times[t] + '</div>';
        for (var d = 0; d < days.length; d++) {
          var key = d + '-' + t;
          var ev = calEvents[key];
          html += '<div class="gsuite-cal-cell">';
          if (ev) {
            html += '<div class="gsuite-cal-event gsuite-cal-event--' + ev.cls + '">' + ev.text + '</div>';
          }
          html += '</div>';
        }
      }
      calGrid.innerHTML = html;
    }
  })();
  </script>
"""

# Read file
with open('/home/user/workspace/jackhagler-portfolio/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# 1. Find the line with "</style>" and insert CSS before it
style_close_idx = None
for i, line in enumerate(lines):
    if '</style>' in line and i > 100:
        style_close_idx = i
        break

if style_close_idx is None:
    raise Exception("Could not find </style>")

# Insert CSS before </style>
lines.insert(style_close_idx, CSS_BLOCK)

# After insertion, line numbers shifted. Re-find things.
content_after_css = '\n'.join(lines)

# 2. Insert HTML between TaxDome demo end and Published Research
# Find the exact markers
insert_marker = '        <!-- Published Research -->'
if insert_marker not in content_after_css:
    raise Exception("Could not find Published Research marker")

content_after_html = content_after_css.replace(
    insert_marker,
    HTML_BLOCK + '\n' + insert_marker
)

# 3. Insert JS right after the TaxDome JS </script> block
# We look for the TaxDome JS ending pattern
taxdome_js_end = "    renderPipeline();\n  })();\n  </script>"
if taxdome_js_end not in content_after_html:
    raise Exception("Could not find TaxDome JS end marker")

content_final = content_after_html.replace(
    taxdome_js_end,
    taxdome_js_end + '\n' + JS_BLOCK
)

# Write back
with open('/home/user/workspace/jackhagler-portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(content_final)

print("Successfully inserted Google Suite CSS, HTML, and JS!")
print(f"Original line count: {len(content.split(chr(10)))}")
print(f"New line count: {len(content_final.split(chr(10)))}") 
