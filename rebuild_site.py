#!/usr/bin/env python3
"""Rebuild index.html with all user-requested changes."""

import re

# Read current files
with open('index.html', 'r') as f:
    html = f.read()

with open('styles.css', 'r') as f:
    css = f.read()

with open('app.js', 'r') as f:
    js = f.read()

# ============================================================
# 1. LOGO: Replace text logo with real image in navbar
# ============================================================
old_logo = '''      <!-- Brand Logo -->
      <a href="#" class="flex items-center gap-3 group">
        <div class="flex items-center gap-1 bg-white px-4 py-2 rounded-2xl shadow-md border border-slate-100 group-hover:shadow-lg transition-shadow">
          <span class="font-display font-black text-2xl tracking-tight text-rose-500">h</span>
          <span class="font-display font-black text-2xl tracking-tight text-amber-500">I</span>
          <span class="font-display font-black text-2xl tracking-tight text-sky-500">P</span>
          <span class="font-display font-black text-2xl tracking-tight text-purple-500">l</span>
          <span class="font-display font-black text-2xl tracking-tight text-rose-500">a</span>
          <span class="font-display font-black text-2xl tracking-tight text-emerald-500">y</span>
        </div>
        <div class="hidden sm:flex flex-col">
          <span class="text-[10px] font-bold uppercase tracking-widest text-slate-400">Indonesia's IP Playground</span>
          <span class="text-xs font-extrabold text-slate-800 flex items-center gap-1">
            by Provaliant Studios <i data-lucide="sparkle" class="w-3 h-3 text-amber-500 fill-amber-400"></i>
          </span>
        </div>
      </a>'''

new_logo = '''      <!-- Brand Logo -->
      <a href="#" class="flex items-center gap-3 group">
        <img src="img/logo-hiplay.png" alt="hIPlay - Indonesia's IP Playground" class="h-10 sm:h-12 w-auto object-contain" />
        <div class="hidden sm:flex flex-col">
          <span class="text-[10px] font-bold uppercase tracking-widest text-slate-400">Indonesia's IP Playground</span>
          <span class="text-xs font-extrabold text-slate-800 flex items-center gap-1">
            by Provaliant Studios <i data-lucide="sparkle" class="w-3 h-3 text-amber-500 fill-amber-400"></i>
          </span>
        </div>
      </a>'''

html = html.replace(old_logo, new_logo)

# ============================================================
# 2. MENU: Simplify navigation - remove Mascots, Deck Explorer
# ============================================================
old_nav = '''      <!-- Desktop Nav Links -->
      <nav class="hidden lg:flex items-center gap-7 text-xs font-bold text-slate-600">
        <a href="#about" class="hover:text-rose-500 transition-colors">The Vision</a>
        <a href="#engine" class="hover:text-rose-500 transition-colors">Platform Engine</a>
        <a href="#featured-ips" class="hover:text-rose-500 transition-colors">IP Universe</a>
        <a href="#mascots" class="hover:text-rose-500 transition-colors">Live Mascots</a>
        <a href="#services" class="hover:text-rose-500 transition-colors">Services</a>
        <a href="#merchandise" class="hover:text-rose-500 transition-colors">Merchandise</a>
        <a href="#deck-viewer" class="hover:text-rose-500 transition-colors">Deck Explorer</a>
        <a href="#contact" class="hover:text-rose-500 transition-colors">Contact</a>
      </nav>'''

new_nav = '''      <!-- Desktop Nav Links -->
      <nav class="hidden lg:flex items-center gap-7 text-xs font-bold text-slate-600">
        <a href="#featured-ips" class="hover:text-rose-500 transition-colors">Featured IPs</a>
        <a href="#merchandise" class="hover:text-rose-500 transition-colors">Merchandise</a>
        <a href="#services" class="hover:text-rose-500 transition-colors">Services</a>
        <a href="#contact" class="hover:text-rose-500 transition-colors">Contact</a>
      </nav>'''

html = html.replace(old_nav, new_nav)

# Remove Deck button from header action buttons
old_action = '''      <!-- Action Buttons -->
      <div class="flex items-center gap-3">
        <button onclick="hIPlayApp.openDeckModal(1)" class="hidden sm:inline-flex items-center gap-1.5 py-2.5 px-4 rounded-xl border border-slate-200 text-slate-700 hover:bg-slate-50 text-xs font-bold transition-all shadow-sm">
          <i data-lucide="presentation" class="w-4 h-4 text-slate-500"></i>
          <span>Deck (35 Slides)</span>
        </button>
        <a href="#contact" class="inline-flex items-center gap-2 py-2.5 px-5 rounded-xl bg-slate-900 hover:bg-rose-500 text-white text-xs font-bold transition-all shadow-md hover:shadow-lg">
          <span>Partner With Us</span>
          <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
        </a>
      </div>'''

new_action = '''      <!-- Action Buttons -->
      <div class="flex items-center gap-3">
        <a href="#contact" class="inline-flex items-center gap-2 py-2.5 px-5 rounded-xl bg-slate-900 hover:bg-rose-500 text-white text-xs font-bold transition-all shadow-md hover:shadow-lg">
          <span>Partner With Us</span>
          <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
        </a>
      </div>'''

html = html.replace(old_action, new_action)

# Remove "View Deck" button from announcement bar
html = html.replace(
    '''    <button onclick="hIPlayApp.openDeckModal(1)" class="hidden md:inline-flex items-center gap-1 bg-white/20 hover:bg-white/30 px-2.5 py-0.5 rounded-full backdrop-blur-md transition-colors text-[11px]">
      <span>View Deck</span> <i data-lucide="arrow-up-right" class="w-3 h-3"></i>
    </button>''',
    ''
)

# ============================================================
# 3. HERO CTA: Remove deck button, simplify
# ============================================================
old_cta = '''        <!-- CTA Action Group -->
        <div class="flex flex-wrap items-center gap-4 mb-14">
          <a href="#featured-ips" class="py-4 px-8 rounded-2xl bg-gradient-to-r from-rose-500 via-amber-500 to-rose-500 text-white text-sm font-bold shadow-lg hover:shadow-xl hover:opacity-95 transition-all flex items-center gap-2.5 candy-shadow">
            <i data-lucide="sparkles" class="w-4 h-4"></i>
            <span>Explore 8+ Featured IPs</span>
          </a>
          <button onclick="hIPlayApp.openDeckModal(1)" class="py-4 px-7 rounded-2xl bg-white border border-slate-200/90 text-slate-800 text-sm font-bold shadow-sm hover:shadow-md hover:bg-slate-50 transition-all flex items-center gap-2">
            <i data-lucide="play-circle" class="w-4 h-4 text-sky-500"></i>
            <span>Interactive 35-Slide Deck</span>
          </button>
          <a href="#contact" class="py-4 px-6 rounded-2xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-sm font-bold transition-colors flex items-center gap-2">
            <span>Become a City Host</span>
            <i data-lucide="building-2" class="w-4 h-4 text-slate-500"></i>
          </a>
        </div>'''

new_cta = '''        <!-- CTA Action Group -->
        <div class="flex flex-wrap items-center gap-4 mb-14">
          <a href="#featured-ips" class="py-4 px-8 rounded-2xl bg-gradient-to-r from-rose-500 via-amber-500 to-rose-500 text-white text-sm font-bold shadow-lg hover:shadow-xl hover:opacity-95 transition-all flex items-center gap-2.5 candy-shadow">
            <i data-lucide="sparkles" class="w-4 h-4"></i>
            <span>Explore Featured IPs</span>
          </a>
          <a href="#merchandise" class="py-4 px-7 rounded-2xl bg-white border border-slate-200/90 text-slate-800 text-sm font-bold shadow-sm hover:shadow-md hover:bg-slate-50 transition-all flex items-center gap-2">
            <i data-lucide="shopping-bag" class="w-4 h-4 text-sky-500"></i>
            <span>View Merchandise</span>
          </a>
          <a href="#contact" class="py-4 px-6 rounded-2xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-sm font-bold transition-colors flex items-center gap-2">
            <span>Become a City Host</span>
            <i data-lucide="building-2" class="w-4 h-4 text-slate-500"></i>
          </a>
        </div>'''

html = html.replace(old_cta, new_cta)

# ============================================================
# 4. FEATURED IP ROSTER: Replace emoji with real character images
# ============================================================
old_roster = '''        <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3">
          <div onclick="hIPlayApp.openIPModal('panji')" class="cursor-pointer p-3 rounded-2xl bg-amber-50 hover:bg-amber-100/80 border border-amber-200/60 transition-all text-center group">
            <span class="text-2xl block mb-1">🌟</span>
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-amber-700">Panji Universe</span>
            <span class="text-[10px] text-amber-600 font-semibold">UNESCO Heritage</span>
          </div>
          <div onclick="hIPlayApp.openIPModal('milk-mocha')" class="cursor-pointer p-3 rounded-2xl bg-rose-50 hover:bg-rose-100/80 border border-rose-200/60 transition-all text-center group">
            <span class="text-2xl block mb-1">🐻</span>
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-rose-700">Milk Mocha</span>
            <span class="text-[10px] text-rose-600 font-semibold">1M+ Global Fans</span>
          </div>
          <div onclick="hIPlayApp.openIPModal('si-juki')" class="cursor-pointer p-3 rounded-2xl bg-yellow-50 hover:bg-yellow-100/80 border border-yellow-200/60 transition-all text-center group">
            <span class="text-2xl block mb-1">👑</span>
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-yellow-700">Si Juki</span>
            <span class="text-[10px] text-yellow-600 font-semibold">#1 Comic Icon</span>
          </div>
          <div onclick="hIPlayApp.openIPModal('hai-dudu')" class="cursor-pointer p-3 rounded-2xl bg-purple-50 hover:bg-purple-100/80 border border-purple-200/60 transition-all text-center group">
            <span class="text-2xl block mb-1">✨</span>
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-purple-700">Hai Dudu</span>
            <span class="text-[10px] text-purple-600 font-semibold">Viral Wholesome</span>
          </div>
          <div onclick="hIPlayApp.openIPModal('fun-cican')" class="cursor-pointer p-3 rounded-2xl bg-sky-50 hover:bg-sky-100/80 border border-sky-200/60 transition-all text-center group">
            <span class="text-2xl block mb-1">📚</span>
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-sky-700">Fun Cican</span>
            <span class="text-[10px] text-sky-600 font-semibold">55 Storybooks</span>
          </div>
          <div onclick="hIPlayApp.openIPModal('kidbash')" class="cursor-pointer p-3 rounded-2xl bg-blue-50 hover:bg-blue-100/80 border border-blue-200/60 transition-all text-center group">
            <span class="text-2xl block mb-1">⚡</span>
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-blue-700">Kidbash</span>
            <span class="text-[10px] text-blue-600 font-semibold">Arcade Hero</span>
          </div>
          <div onclick="hIPlayApp.openIPModal('dino-island')" class="cursor-pointer p-3 rounded-2xl bg-emerald-50 hover:bg-emerald-100/80 border border-emerald-200/60 transition-all text-center group">
            <span class="text-2xl block mb-1">🦖</span>
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-emerald-700">Dino Island</span>
            <span class="text-[10px] text-emerald-600 font-semibold">Prehistoric SciFi</span>
          </div>
          <div onclick="hIPlayApp.openIPModal('bona')" class="cursor-pointer p-3 rounded-2xl bg-pink-50 hover:bg-pink-100/80 border border-pink-200/60 transition-all text-center group">
            <span class="text-2xl block mb-1">🐘</span>
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-pink-700">Bona &amp; Friends</span>
            <span class="text-[10px] text-pink-600 font-semibold">Bobo Heritage</span>
          </div>
        </div>'''

new_roster = '''        <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3">
          <div onclick="hIPlayApp.openIPModal('panji')" class="cursor-pointer p-2 rounded-2xl bg-amber-50 hover:bg-amber-100/80 border border-amber-200/60 transition-all text-center group hover:shadow-md">
            <div class="w-full h-20 rounded-xl overflow-hidden bg-white mb-1.5">
              <img src="img/char-panji.jpg" alt="Legenda Panji" class="w-full h-full object-contain" />
            </div>
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-amber-700">Panji Universe</span>
            <span class="text-[10px] text-amber-600 font-semibold">UNESCO Heritage</span>
          </div>
          <div onclick="hIPlayApp.openIPModal('milk-mocha')" class="cursor-pointer p-2 rounded-2xl bg-rose-50 hover:bg-rose-100/80 border border-rose-200/60 transition-all text-center group hover:shadow-md">
            <div class="w-full h-20 rounded-xl overflow-hidden bg-white mb-1.5">
              <img src="img/char-milk-mocha.jpg" alt="Milk Mocha Bear" class="w-full h-full object-contain" />
            </div>
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-rose-700">Milk Mocha</span>
            <span class="text-[10px] text-rose-600 font-semibold">1M+ Global Fans</span>
          </div>
          <div onclick="hIPlayApp.openIPModal('si-juki')" class="cursor-pointer p-2 rounded-2xl bg-yellow-50 hover:bg-yellow-100/80 border border-yellow-200/60 transition-all text-center group hover:shadow-md">
            <div class="w-full h-20 rounded-xl overflow-hidden bg-white mb-1.5">
              <img src="img/char-si-juki.jpg" alt="Si Juki" class="w-full h-full object-contain" />
            </div>
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-yellow-700">Si Juki</span>
            <span class="text-[10px] text-yellow-600 font-semibold">#1 Comic Icon</span>
          </div>
          <div onclick="hIPlayApp.openIPModal('hai-dudu')" class="cursor-pointer p-2 rounded-2xl bg-purple-50 hover:bg-purple-100/80 border border-purple-200/60 transition-all text-center group hover:shadow-md">
            <div class="w-full h-20 rounded-xl overflow-hidden bg-white mb-1.5">
              <img src="img/char-hai-dudu.jpg" alt="Hai Dudu" class="w-full h-full object-contain" />
            </div>
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-purple-700">Hai Dudu</span>
            <span class="text-[10px] text-purple-600 font-semibold">Viral Wholesome</span>
          </div>
          <div onclick="hIPlayApp.openIPModal('fun-cican')" class="cursor-pointer p-2 rounded-2xl bg-sky-50 hover:bg-sky-100/80 border border-sky-200/60 transition-all text-center group hover:shadow-md">
            <div class="w-full h-20 rounded-xl overflow-hidden bg-white mb-1.5">
              <img src="img/char-fun-cican.jpg" alt="Fun Cican" class="w-full h-full object-contain" />
            </div>
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-sky-700">Fun Cican</span>
            <span class="text-[10px] text-sky-600 font-semibold">55 Storybooks</span>
          </div>
          <div onclick="hIPlayApp.openIPModal('kidbash')" class="cursor-pointer p-2 rounded-2xl bg-blue-50 hover:bg-blue-100/80 border border-blue-200/60 transition-all text-center group hover:shadow-md">
            <div class="w-full h-20 rounded-xl overflow-hidden bg-white mb-1.5">
              <img src="img/char-kidbash.jpg" alt="Kidbash" class="w-full h-full object-contain" />
            </div>
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-blue-700">Kidbash</span>
            <span class="text-[10px] text-blue-600 font-semibold">Arcade Hero</span>
          </div>
          <div onclick="hIPlayApp.openIPModal('dino-island')" class="cursor-pointer p-2 rounded-2xl bg-emerald-50 hover:bg-emerald-100/80 border border-emerald-200/60 transition-all text-center group hover:shadow-md">
            <div class="w-full h-20 rounded-xl overflow-hidden bg-white mb-1.5">
              <img src="img/char-dino-island.jpg" alt="Dino Island" class="w-full h-full object-contain" />
            </div>
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-emerald-700">Dino Island</span>
            <span class="text-[10px] text-emerald-600 font-semibold">Prehistoric SciFi</span>
          </div>
          <div onclick="hIPlayApp.openIPModal('bona')" class="cursor-pointer p-2 rounded-2xl bg-pink-50 hover:bg-pink-100/80 border border-pink-200/60 transition-all text-center group hover:shadow-md">
            <div class="w-full h-20 rounded-xl overflow-hidden bg-white mb-1.5">
              <img src="img/char-bona.jpg" alt="Bona &amp; Friends" class="w-full h-full object-contain" />
            </div>
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-pink-700">Bona &amp; Friends</span>
            <span class="text-[10px] text-pink-600 font-semibold">Bobo Heritage</span>
          </div>
        </div>'''

html = html.replace(old_roster, new_roster)

# ============================================================
# 5. RE-ARRANGE: Swap Vision (about) and Platform Engine order
#    Currently: Engine (section id=engine) comes BEFORE About (section id=about)
#    New order: About first, then Engine
# ============================================================
# Extract both sections
engine_start = html.find('  <!-- Platform Engine / Flywheel Section -->')
engine_end = html.find('  <!-- Section: National Mission & Creative Economy -->')
about_start = engine_end
about_end = html.find('  <!-- Section: Featured IP Showcase & Filterable Hub -->')

engine_section = html[engine_start:engine_end]
about_section = html[about_start:about_end]

# Swap them
html = html[:engine_start] + about_section + engine_section + html[about_end:]

# ============================================================
# 6. REMOVE: Live Mascots section (id=mascots)
# ============================================================
mascots_start = html.find('  <!-- Mascot Real-Life Activations -->')
mascots_end = html.find('  <!-- Provaliant Studios & Business Solutions -->')
if mascots_start > 0 and mascots_end > 0:
    html = html[:mascots_start] + html[mascots_end:]

# ============================================================
# 7. MERCHANDISE: Expand to show all 8 IPs
# ============================================================
old_merch = '''      <!-- Merchandise Preview Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        
        <div class="bg-white rounded-3xl overflow-hidden border border-slate-200/80 shadow-sm hover:shadow-xl transition-all group">
          <div class="h-64 overflow-hidden bg-slate-100">
            <img src="img/Untitled copy_page-0016.jpg" alt="Milk Mocha Merch" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          </div>
          <div class="p-6">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-bold text-rose-600">Milk Mocha Bear</span>
              <span class="text-[10px] text-slate-400 font-medium">Slide 16</span>
            </div>
            <h4 class="text-lg font-bold text-slate-900 mb-2">Pastel Lifestyle & Drinkware</h4>
            <p class="text-xs text-slate-500 leading-relaxed">
              Tote bags, vacuum tumblers, caps, plush keychains, and cosmetic pouches designed for young couples and fans.
            </p>
          </div>
        </div>

        <div class="bg-white rounded-3xl overflow-hidden border border-slate-200/80 shadow-sm hover:shadow-xl transition-all group">
          <div class="h-64 overflow-hidden bg-slate-100">
            <img src="img/Untitled copy_page-0019.jpg" alt="Si Juki Merch" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          </div>
          <div class="p-6">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-bold text-yellow-600">Si Juki</span>
              <span class="text-[10px] text-slate-400 font-medium">Slide 19</span>
            </div>
            <h4 class="text-lg font-bold text-slate-900 mb-2">Streetwear & Hustle Apparel</h4>
            <p class="text-xs text-slate-500 leading-relaxed">
              "Kerja Keras / Scroll Lebih Keras" graphic tees, "Out of the Box" totes, overthinking caps, and acrylic charms.
            </p>
          </div>
        </div>

        <div class="bg-white rounded-3xl overflow-hidden border border-slate-200/80 shadow-sm hover:shadow-xl transition-all group">
          <div class="h-64 overflow-hidden bg-slate-100">
            <img src="img/Untitled copy_page-0028.jpg" alt="Kidbash Merch" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          </div>
          <div class="p-6">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-bold text-blue-600">Kidbash</span>
              <span class="text-[10px] text-slate-400 font-medium">Slide 28</span>
            </div>
            <h4 class="text-lg font-bold text-slate-900 mb-2">Arcade Gamer Gear & Bottles</h4>
            <p class="text-xs text-slate-500 leading-relaxed">
              "Insert Coin" vintage-look tees, Kidbash Energy water bottles, pixel-art acrylic charms, and messenger bags.
            </p>
          </div>
        </div>

      </div>'''

new_merch = '''      <!-- Merchandise Preview Cards - All 8 IPs -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <div class="bg-white rounded-3xl overflow-hidden border border-slate-200/80 shadow-sm hover:shadow-xl transition-all group cursor-pointer" onclick="hIPlayApp.openIPModal('panji')">
          <div class="h-52 overflow-hidden bg-slate-100">
            <img src="img/slide-07.jpg" alt="Legenda Panji Merch" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          </div>
          <div class="p-5">
            <span class="text-xs font-bold text-amber-600">Legenda Panji</span>
            <h4 class="text-base font-bold text-slate-900 mb-1 mt-1">Heritage Plushies & Apparel</h4>
            <p class="text-[11px] text-slate-500 leading-relaxed">Krucil character tumblers, graphic tees, plush keychains & mascot cushions.</p>
          </div>
        </div>

        <div class="bg-white rounded-3xl overflow-hidden border border-slate-200/80 shadow-sm hover:shadow-xl transition-all group cursor-pointer" onclick="hIPlayApp.openIPModal('milk-mocha')">
          <div class="h-52 overflow-hidden bg-slate-100">
            <img src="img/slide-16.jpg" alt="Milk Mocha Merch" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          </div>
          <div class="p-5">
            <span class="text-xs font-bold text-rose-600">Milk Mocha Bear</span>
            <h4 class="text-base font-bold text-slate-900 mb-1 mt-1">Pastel Lifestyle & Drinkware</h4>
            <p class="text-[11px] text-slate-500 leading-relaxed">Tote bags, vacuum tumblers, caps, plush keychains & cosmetic pouches.</p>
          </div>
        </div>

        <div class="bg-white rounded-3xl overflow-hidden border border-slate-200/80 shadow-sm hover:shadow-xl transition-all group cursor-pointer" onclick="hIPlayApp.openIPModal('si-juki')">
          <div class="h-52 overflow-hidden bg-slate-100">
            <img src="img/slide-19.jpg" alt="Si Juki Merch" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          </div>
          <div class="p-5">
            <span class="text-xs font-bold text-yellow-600">Si Juki</span>
            <h4 class="text-base font-bold text-slate-900 mb-1 mt-1">Streetwear & Hustle Apparel</h4>
            <p class="text-[11px] text-slate-500 leading-relaxed">"Kerja Keras" graphic tees, "Out of the Box" totes & acrylic charms.</p>
          </div>
        </div>

        <div class="bg-white rounded-3xl overflow-hidden border border-slate-200/80 shadow-sm hover:shadow-xl transition-all group cursor-pointer" onclick="hIPlayApp.openIPModal('hai-dudu')">
          <div class="h-52 overflow-hidden bg-slate-100">
            <img src="img/slide-22.jpg" alt="Hai Dudu Merch" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          </div>
          <div class="p-5">
            <span class="text-xs font-bold text-purple-600">Hai Dudu</span>
            <h4 class="text-base font-bold text-slate-900 mb-1 mt-1">Pastel Sling Bags & Apparel</h4>
            <p class="text-[11px] text-slate-500 leading-relaxed">Crossbody sling bags, pastel graphic tees, tumblers & cosmetic pouches.</p>
          </div>
        </div>

        <div class="bg-white rounded-3xl overflow-hidden border border-slate-200/80 shadow-sm hover:shadow-xl transition-all group cursor-pointer" onclick="hIPlayApp.openIPModal('fun-cican')">
          <div class="h-52 overflow-hidden bg-slate-100">
            <img src="img/slide-25.jpg" alt="Fun Cican Merch" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          </div>
          <div class="p-5">
            <span class="text-xs font-bold text-sky-600">Fun Cican</span>
            <h4 class="text-base font-bold text-slate-900 mb-1 mt-1">Kids Bags & School Gear</h4>
            <p class="text-[11px] text-slate-500 leading-relaxed">Drawstring backpacks, school totes, leak-proof tumblers & pencil cases.</p>
          </div>
        </div>

        <div class="bg-white rounded-3xl overflow-hidden border border-slate-200/80 shadow-sm hover:shadow-xl transition-all group cursor-pointer" onclick="hIPlayApp.openIPModal('kidbash')">
          <div class="h-52 overflow-hidden bg-slate-100">
            <img src="img/slide-28.jpg" alt="Kidbash Merch" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          </div>
          <div class="p-5">
            <span class="text-xs font-bold text-blue-600">Kidbash</span>
            <h4 class="text-base font-bold text-slate-900 mb-1 mt-1">Arcade Gamer Gear & Bottles</h4>
            <p class="text-[11px] text-slate-500 leading-relaxed">"Insert Coin" tees, energy bottles, pixel-art charms & messenger bags.</p>
          </div>
        </div>

        <div class="bg-white rounded-3xl overflow-hidden border border-slate-200/80 shadow-sm hover:shadow-xl transition-all group cursor-pointer" onclick="hIPlayApp.openIPModal('dino-island')">
          <div class="h-52 overflow-hidden bg-slate-100">
            <img src="img/slide-11.jpg" alt="Dino Island Merch" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          </div>
          <div class="p-5">
            <span class="text-xs font-bold text-emerald-600">Dino Island</span>
            <h4 class="text-base font-bold text-slate-900 mb-1 mt-1">Explorer Gear & Dino Mugs</h4>
            <p class="text-[11px] text-slate-500 leading-relaxed">Roll-top backpacks, team jerseys, sculpted dino mugs & explorer badges.</p>
          </div>
        </div>

        <div class="bg-white rounded-3xl overflow-hidden border border-slate-200/80 shadow-sm hover:shadow-xl transition-all group cursor-pointer" onclick="hIPlayApp.openIPModal('bona')">
          <div class="h-52 overflow-hidden bg-slate-100">
            <img src="img/slide-31.jpg" alt="Bona & Friends Merch" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          </div>
          <div class="p-5">
            <span class="text-xs font-bold text-pink-600">Bona & Friends</span>
            <h4 class="text-base font-bold text-slate-900 mb-1 mt-1">Pastel Lifestyle & Heritage</h4>
            <p class="text-[11px] text-slate-500 leading-relaxed">Illustration tote bags, tie-dye tees, patterned tumblers & acrylic keyrings.</p>
          </div>
        </div>

      </div>'''

html = html.replace(old_merch, new_merch)

# ============================================================
# 8. REMOVE: Deck Explorer section + Deck modal
# ============================================================
deck_section_start = html.find('  <!-- Interactive Slide Deck Viewer Section -->')
deck_section_end = html.find('  <!-- Partnership & Contact Hub Section -->')
if deck_section_start > 0 and deck_section_end > 0:
    html = html[:deck_section_start] + html[deck_section_end:]

# Remove deck modal
deck_modal_start = html.find('  <!-- Modal: 35-Slide Deck Fullscreen Viewer -->')
deck_modal_end = html.find('  <!-- Scripts -->')
if deck_modal_start > 0 and deck_modal_end > 0:
    html = html[:deck_modal_start] + '\n' + html[deck_modal_end:]

# ============================================================
# 9. FOOTER: Update with real logo and simplified links
# ============================================================
old_footer_links = '''      <div class="flex items-center gap-3">
        <span class="font-display font-black text-xl text-rose-500">hIPlay</span>
        <span class="text-slate-300">|</span>
        <span class="text-slate-600 font-semibold">Indonesia's IP Playground by Provaliant Studios</span>
      </div>

      <div class="flex items-center gap-6 font-semibold">
        <a href="#about" class="hover:text-slate-900 transition-colors">The Vision</a>
        <a href="#featured-ips" class="hover:text-slate-900 transition-colors">IP Universe</a>
        <a href="#mascots" class="hover:text-slate-900 transition-colors">Mascots</a>
        <a href="#services" class="hover:text-slate-900 transition-colors">Services</a>
        <a href="#contact" class="hover:text-slate-900 transition-colors">Contact</a>
      </div>'''

new_footer_links = '''      <div class="flex items-center gap-3">
        <img src="img/logo-hiplay.png" alt="hIPlay" class="h-8 w-auto" />
        <span class="text-slate-300">|</span>
        <span class="text-slate-600 font-semibold">Indonesia's IP Playground by Provaliant Studios</span>
      </div>

      <div class="flex items-center gap-6 font-semibold">
        <a href="#featured-ips" class="hover:text-slate-900 transition-colors">Featured IPs</a>
        <a href="#merchandise" class="hover:text-slate-900 transition-colors">Merchandise</a>
        <a href="#services" class="hover:text-slate-900 transition-colors">Services</a>
        <a href="#contact" class="hover:text-slate-900 transition-colors">Contact</a>
      </div>'''

html = html.replace(old_footer_links, new_footer_links)

# ============================================================
# 10. FIX: Update remaining "Untitled copy" image references
# ============================================================
def fix_img_ref(m):
    num = int(m.group(1))
    return f'img/slide-{num:02d}.jpg'

html = re.sub(r'img/Untitled copy_page-(\d{4})\.jpg', fix_img_ref, html)

# ============================================================
# 11. Remove "View Slide 2 Details" and "View Slide 34 Matrix" buttons
# ============================================================
html = html.replace(
    '''            <button onclick="hIPlayApp.openDeckModal(2)" class="text-xs font-bold text-rose-600 hover:underline flex items-center gap-1">
              <span>View Slide 2 Details</span> <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </button>''',
    ''
)

html = html.replace(
    '''          <button onclick="hIPlayApp.openDeckModal(34)" class="text-xs font-bold text-rose-400 hover:underline flex items-center gap-1">
            <span>View Slide 34 Matrix ↗</span>
          </button>''',
    ''
)

# ============================================================
# 12. Re-inline CSS and JS for self-contained file:/// use
# ============================================================
# The inlined <style> and <script> blocks are already in the HTML from earlier
# We just need to make sure the inlined JS is updated too

# Find and replace the inlined script content
inline_script_start = html.find('  <script>\n/**\n * hIPlay Minisite')
if inline_script_start > 0:
    inline_script_end = html.find('  </script>\n</body>')
    if inline_script_end > 0:
        html = html[:inline_script_start] + '  <script>\n' + js + '\n  </script>\n' + html[inline_script_end + len('  </script>\n'):]

# Write the final HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ index.html rebuilt successfully!")
print("Changes applied:")
print("  1. Real hIPlay logo in navbar and footer")
print("  2. Simplified menu (Featured IPs, Merchandise, Services, Contact)")
print("  3. Removed Deck Explorer section & modal")
print("  4. Removed Live Mascots section")
print("  5. Merchandise section expanded to all 8 IPs")
print("  6. Featured IP Roster uses real character images")
print("  7. Re-arranged Vision before Platform Engine")
print("  8. Fixed all image paths")
print("  9. Self-contained with inlined CSS/JS")
