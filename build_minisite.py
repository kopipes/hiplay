# Generator for hIPlay Minisite
import os

app_js_content = """/**
 * hIPlay Minisite - Interactive JavaScript Engine
 * Provaliant Studios & hIPlay Experience Platform
 */

const IP_DATABASE = [
  {
    id: 'panji',
    name: 'Legenda Panji Universe',
    studio: 'Provaliant Studios Original',
    type: 'original',
    categoryTag: 'Original IP • UNESCO Heritage',
    badge: '🌟 Flagship Original IP',
    accentColor: '#D97706',
    tagline: 'A World Where Stories Come to Life & East Javanese Legends Awaken',
    summary: 'Reimagines the timeless East Javanese legend recognized by UNESCO for modern audiences—expanding into films, animation, merchandise, and immersive experiences.',
    theme: 'The Panji Universe is a world where stories are not merely fairy tales, but the source of life\\'s energy. As long as humans continue to tell stories, the Realm of Legends remains alive. At the center stands the Dewandaru Tree, the source of all Nusantara legends. When cut down by Jagad Peteng, the world of stories began to crumble, and a new generation of Panji must be found to bring it back to life.',
    background: 'PROVALIANT STUDIO\\'s flagship original IP, Legenda Panji Universe, reimagines East Javanese folklore into a global franchise. With strong expertise in licensed merchandise, IP collaborations, and brand activations, Provaliant is committed to revitalizing local stories as a symbol of the rising creative spirit of the Nusantara.',
    characters: ['Panji (Nusantara Hero)', 'Krucil Tigris (White Tiger)', 'Krucil Garuda/Owl (Sage Guardian)', 'Dewandaru Spirits'],
    metrics: [
      { label: 'Heritage', val: 'UNESCO Recognized' },
      { label: 'Scope', val: 'Global Multiverse' },
      { label: 'Formats', val: 'Film, Animation & Merch' }
    ],
    coverImage: 'img/Untitled copy_page-0006.jpg',
    styleGuideImage: 'img/Untitled copy_page-0008.jpg',
    merchImage: 'img/Untitled copy_page-0007.jpg',
    mascotImage: 'img/Untitled copy_page-0009.jpg',
    slides: [6, 7, 8, 9, 34],
    merchHighlights: ['Krucil character tumblers & water bottles', 'Apparel & graphic tees', 'Plush keychains & mascot cushions', 'Tote bags & collector pouches']
  },
  {
    id: 'milk-mocha',
    name: 'Milk Mocha Bear',
    studio: 'Local IP Collaboration',
    type: 'collab',
    categoryTag: 'Global Viral IP • Romance & Lifestyle',
    badge: '🔥 1M+ Global Followers',
    accentColor: '#EA580C',
    tagline: 'Heartwarming Companionship Connecting Over 1 Million Fans Globally',
    summary: 'One of the most viral Indonesian-born character IPs worldwide, featuring Milk & Mocha with a massive 14% engagement rate across the US, India, and Indonesia.',
    theme: 'As Companions, Milk Mocha Bear can be partners, couple, friends, or pals. They complete each other\\'s traits and personalities. They can represent you and your companion through themes of love, emotion, food sharing, and cozy moments.',
    background: 'Launched as LINE sticker characters in 2016, Milk Mocha Bear quickly gained immense global popularity through cute animations and became the first Indonesian creator stickers featured in the Official LINE Sticker MVP Program. Today, Milk Mocha Bear is a global brand with over 1 million followers led by audiences in India, USA, and Indonesia, with a consistent 14% Instagram engagement rate (155.5K likes and 2.5K comments per post).',
    characters: ['Milk (Cheerful White Bear)', 'Mocha (Caring Brown Bear)', 'Matcha (Little Dino Companion)'],
    metrics: [
      { label: 'Global Followers', val: '1,000,000+' },
      { label: 'IG Engagement', val: '14.0% (Avg 1-3%)' },
      { label: 'Avg Likes / Post', val: '155.5K+' }
    ],
    coverImage: 'img/Untitled copy_page-0014.jpg',
    styleGuideImage: 'img/Untitled copy_page-0015.jpg',
    merchImage: 'img/Untitled copy_page-0016.jpg',
    slides: [14, 15, 16],
    merchHighlights: ['Eco-friendly tote bags & commuter canvas bags', 'Double-wall stainless tumblers & pastel flasks', 'Embroidered dad caps & soft pastel tees', 'Couple plushies, keychains & pouch sets']
  },
  {
    id: 'si-juki',
    name: 'Si Juki',
    studio: 'Created by Faza Meonk / PIONICON',
    type: 'collab',
    categoryTag: 'Pop Culture • Youth & Satire',
    badge: '👑 Indonesia\\'s #1 Comic IP',
    accentColor: '#EAB308',
    tagline: 'The Legendary Maverick of Indonesian Pop Culture & Everyday Satire',
    summary: 'Indonesia\\'s most iconic and commercially successful comic character, famous for witty humor, streetwise charm, blockbuster animated movies, and lifestyle streetwear.',
    theme: 'Si Juki is one of Indonesia\\'s most iconic comic characters, known for his witty humor, rebellious charm, and unpredictable way of solving everyday problems from student struggles to modern work hustle.',
    background: 'Born from a sketch in 2010, Si Juki debuted in the bestselling comic \\'Ngampus!!! Buka-bukaan Aib Mahasiswa\\'. Since then, the character has grown into one of Indonesia\\'s leading pop culture IPs, expanding into animated films, TV series, merchandise, apparel, games, and collaborations with brands, media, and government institutions.',
    characters: ['Si Juki', 'Prof. Juned', 'Mang Awung', 'Coro the Cockroach'],
    metrics: [
      { label: 'Debut Year', val: '2010' },
      { label: 'Media Reach', val: 'Theatrical Movies & TV' },
      { label: 'Audience', val: 'Gen Z, Millennials & Youth' }
    ],
    coverImage: 'img/Untitled copy_page-0017.jpg',
    styleGuideImage: 'img/Untitled copy_page-0018.jpg',
    merchImage: 'img/Untitled copy_page-0019.jpg',
    mascotImage: 'img/Untitled copy_page-0004.jpg',
    slides: [17, 18, 19, 4],
    merchHighlights: ['Hustle & \\'Kerja Keras / Scroll Lebih Keras\\' graphic apparel', 'Canvas messenger & \\'Out of the Box\\' tote bags', 'FOMO & \\'Ngutang Dulu\\' acrylic keychains', '\\'Overthinking\\' streetwear dad caps & tumblers']
  },
  {
    id: 'hai-dudu',
    name: 'Hai Dudu',
    studio: 'Local IP Collaboration',
    type: 'collab',
    categoryTag: 'Feel-Good Fandom • Friendship & Joy',
    badge: '✨ Viral Whimsical Friends',
    accentColor: '#8B5CF6',
    tagline: 'Warmth, Laughter, and Everyday Happiness From the Dimension of Fiafia',
    summary: 'A beloved Indonesian character trio that celebrates the pure joy of friendship, goofy humor, and relatable everyday comfort moments.',
    theme: 'Dudu, Bimo, and Sisi are three best friends from Fiafia, a distant dimension who came to Earth and decided to stay. Together, they bring warmth, laughter, and happiness to everyday life through their unique personalities. Dudu finds joy in the little things, Bimo charms everyone with his lovable cluelessness, and Sisi keeps the trio balanced with her wit and caring nature.',
    background: 'Their relatable adventures have made Hai Dudu a beloved Indonesian IP that celebrates friendship and everyday happiness across digital stickers and viral content.',
    characters: ['Dudu (Joyful Orange Buddy)', 'Bimo (Lovably Clueless White Cloud)', 'Sisi (Witty Pink Bestie)'],
    metrics: [
      { label: 'Origin', val: 'Fiafia Dimension' },
      { label: 'Core Vibe', val: 'Warmth & Wholesome Fun' },
      { label: 'Target', val: 'Teens, Young Adults & Kids' }
    ],
    coverImage: 'img/Untitled copy_page-0020.jpg',
    styleGuideImage: 'img/Untitled copy_page-0021.jpg',
    merchImage: 'img/Untitled copy_page-0022.jpg',
    mascotImage: 'img/Untitled copy_page-0004.jpg',
    slides: [20, 21, 22, 4],
    merchHighlights: ['Dudu & Bimo crossbody sling bags', 'Pastel graphic tees & daily apparel', 'Collector tumbler series with character expressions', 'Cute keychains, pastel caps & cosmetic pouches']
  },
  {
    id: 'fun-cican',
    name: 'Fun Cican',
    studio: 'Local IP Collaboration',
    type: 'collab',
    categoryTag: 'Early Childhood • Edutainment',
    badge: '📚 55 Published Storybooks',
    accentColor: '#0EA5E9',
    tagline: 'Empowering Children\\'s Imagination with 1,000+ Character World',
    summary: 'A multi-award winning early childhood ecosystem featuring animated series, TikTok micro-content, 55 published storybook titles, and original sing-along songs.',
    theme: 'Fun Cican is part of M.C. Bunny (Mushroom Cut Bunny), spreading kindness, creativity, positive habits, and musical adventures to children and young families.',
    background: 'A local Indonesian IP built through an ecosystem of micro-content, including TikTok, animated series, 55 storybook titles, and dozens of original songs. With a roadmap of up to 1,025 characters, the IP is designed to grow into comics, OTT content, games, and other storytelling formats.',
    characters: ['Cican (Mushroom Cut Bunny)', 'Cici', 'Kebon Friends', 'Alien Pals'],
    metrics: [
      { label: 'Storybooks', val: '55 Published Titles' },
      { label: 'Character Roadmap', val: 'Up to 1,025 Characters' },
      { label: 'Formats', val: 'Books, Songs, OTT & Series' }
    ],
    coverImage: 'img/Untitled copy_page-0023.jpg',
    styleGuideImage: 'img/Untitled copy_page-0024.jpg',
    merchImage: 'img/Untitled copy_page-0025.jpg',
    mascotImage: 'img/Untitled copy_page-0004.jpg',
    slides: [23, 24, 25, 4],
    merchHighlights: ['Children drawstring backpacks & school tote bags', 'Playful yellow-and-blue graphic t-shirts', 'Stainless leak-proof school tumblers', 'Character badges, caps & pencil cases']
  },
  {
    id: 'kidbash',
    name: 'Kidbash',
    studio: 'Original Action IP Collaboration',
    type: 'collab',
    categoryTag: 'Action Superhero • Retro Gaming',
    badge: '⚡ Retro Arcade Superhero',
    accentColor: '#2563EB',
    tagline: 'Redefining Heroism for the Forgotten Champions & Gamers',
    summary: 'An adrenaline-fueled retro-arcade superhero narrative speaking for those who were never meant to shine, showing that true heroes are defined by empathy and sacrifice.',
    theme: 'Kidbash is a story about redefining heroism. It speaks for forgotten characters and those who were never meant to shine. True heroes aren\\'t defined by spectacle, but by sacrifice, by what they are willing to give to those in need. Kidbash awakens with no memory of his past, knowing only his name and dream of becoming a hero. After failing to protect Mandala Village, he begins a journey to find the legendary master Tao Shen Long.',
    background: 'Combining 3D video-game aesthetics, retro pixel art nostalgia, and modern superhero storytelling into a high-energy IP universe.',
    characters: ['Kidbash (Heroic Kid)', 'Master Tao Shen Long', 'Mandala Guardians'],
    metrics: [
      { label: 'Visual Style', val: '3D Arcade & Pixel Nostalgia' },
      { label: 'Core Theme', val: 'Empathy, Persistence & Courage' },
      { label: 'Audience', val: 'Gamers, Anime Fans & Youth' }
    ],
    coverImage: 'img/Untitled copy_page-0026.jpg',
    styleGuideImage: 'img/Untitled copy_page-0027.jpg',
    merchImage: 'img/Untitled copy_page-0028.jpg',
    slides: [26, 27, 28],
    merchHighlights: ['Insert Coin & Those Who Are Forgotten gamer tees', 'Cyber-styled heavy-duty tote bags & pouches', 'Kidbash Energy sport bottles & vacuum tumblers', 'Pixel acrylic charm keychains & gamer caps']
  },
  {
    id: 'bona',
    name: 'Bona & Friends',
    studio: 'Classic Indonesian Heritage',
    type: 'collab',
    categoryTag: 'Legendary Nostalgia • Bobo Magazine',
    badge: '🐘 Iconic Childhood Classic',
    accentColor: '#EC4899',
    tagline: 'The Little Pink Elephant with a Magical Trunk Loved Across Generations',
    summary: 'One of the most timeless and beloved Indonesian comic icons in history from Majalah Bobo, modernized for next-generation family entertainment.',
    theme: 'Bona, the little elephant with a magical trunk, is one of the most beloved characters from Bobo Magazine. Together with his best friends, Ola the rabbit and Kaka the cockatoo, Bona helps anyone in need using his trunk, which can transform into various useful tools.',
    background: 'Published continuously for decades in Bobo Magazine, Bona & Friends holds unmatched brand equity and cross-generational nostalgia across millions of Indonesian families.',
    characters: ['Bona (Magical Pink Elephant)', 'Ola (Brave Rabbit)', 'Kaka (Clever Cockatoo)', 'Arka, Lila, Putri, Gavin'],
    metrics: [
      { label: 'Legacy', val: 'Decades of Nostalgia' },
      { label: 'Publication', val: 'Majalah Bobo Flagship' },
      { label: 'Appeal', val: 'Multi-Generational Family' }
    ],
    coverImage: 'img/Untitled copy_page-0029.jpg',
    styleGuideImage: 'img/Untitled copy_page-0030.jpg',
    merchImage: 'img/Untitled copy_page-0031.jpg',
    slides: [29, 30, 31],
    merchHighlights: ['Pastel illustration tote bags & tie-dye tees', 'Character patterned tumblers & water flasks', 'Embroidered purple baseball caps & pouches', 'Collectible acrylic keyrings of Bona, Ola & Kaka']
  },
  {
    id: 'dino-island',
    name: 'Dino Island',
    studio: 'Provaliant Studios Original',
    type: 'original',
    categoryTag: 'Original IP • Edutainment Adventure',
    badge: '🦖 Prehistoric Cyber-Adventure',
    accentColor: '#16A34A',
    tagline: 'Thrilling Prehistoric Adventures, Cyber-Augmented Dinos & Family Fun',
    summary: 'An educational dinosaur adventure series blending live theatrical mascot entertainment, cybernetic prehistoric creatures, and interactive edutainment.',
    theme: 'Educational dinosaur adventure series focusing on merchandising, licensing, social media content with Diby (Dino Baby), and high-impact experiential live entertainment for families.',
    background: 'Original Provaliant Studios franchise developed for immersive mall activations, live animatronic/mascot stage performances, and educational media.',
    characters: ['Diby (Baby Dino)', 'Rex (Cyber T-Rex)', 'Triceratops Guardian', 'Explorer Crew'],
    metrics: [
      { label: 'Format', val: 'Live Stage Shows & Experiential' },
      { label: 'Social Star', val: 'Diby (Dino Baby) Content' },
      { label: 'Market', val: 'Family & Edutainment' }
    ],
    coverImage: 'img/Untitled copy_page-0010.jpg',
    merchImage: 'img/Untitled copy_page-0011.jpg',
    mascotImage: 'img/Untitled copy_page-0004.jpg',
    slides: [10, 11, 4, 34],
    merchHighlights: ['Jungle explorer roll-top backpacks', 'Dino Island Team jerseys & graphic shirts', 'Custom sculpted prehistoric dinosaur mugs', 'Explorer badge caps, lanyards & pins']
  }
];

const ALL_SLIDES = Array.from({ length: 35 }, (_, i) => {
  const num = i + 1;
  const pad = String(num).padStart(4, '0');
  let title = 'hIPlay Presentation Deck - Slide ' + num;
  let category = 'Overview';
  
  if (num === 1) { title = 'Introducing hIPlay - Indonesia\\'s IP Playground'; category = 'Intro'; }
  else if (num === 2) { title = 'Our Mission: Boosting Indonesia\\'s Creative Economy'; category = 'Mission'; }
  else if (num === 3) { title = 'Featured IPs Roster - Expanding Audience Spectrum'; category = 'Roster'; }
  else if (num === 4) { title = 'Featured IPs - Character Mascot Costumes & Activations'; category = 'Mascots'; }
  else if (num === 5) { title = 'Section 1: Our Original IPs (Provaliant Studios)'; category = 'Original IP'; }
  else if (num === 6) { title = 'Legenda Panji Universe - A World Where Stories Come to Life'; category = 'Panji Universe'; }
  else if (num === 7) { title = 'Legenda Panji (Krucil) - IP Merchandise Concept'; category = 'Merchandise'; }
  else if (num === 8) { title = 'Legenda Panji - Plushies, Keychains & Apparel Preview'; category = 'Merchandise'; }
  else if (num === 9) { title = 'Legenda Panji - Live Mascot Stage Activation'; category = 'Mascots'; }
  else if (num === 10) { title = 'Dino Island - Key Visual & Explorer Universe'; category = 'Dino Island'; }
  else if (num === 11) { title = 'Dino Island - Adventure Gear & Merchandise Line'; category = 'Merchandise'; }
  else if (num === 12) { title = 'Section 2: IP Collaborations (Leading Local IPs)'; category = 'Collaborations'; }
  else if (num === 13) { title = 'IP Collaboration Partners Overview'; category = 'Collaborations'; }
  else if (num === 14) { title = 'Milk Mocha Bear - Theme, Global Reach & Social Stats'; category = 'Milk Mocha'; }
  else if (num === 15) { title = 'Milk Mocha Bear - IP Style Guide (Love, Food, Sleep)'; category = 'Style Guide'; }
  else if (num === 16) { title = 'Milk Mocha Bear - Merchandise Collection Preview'; category = 'Merchandise'; }
  else if (num === 17) { title = 'Si Juki - Theme, Background & Pop Culture Legacy'; category = 'Si Juki'; }
  else if (num === 18) { title = 'Si Juki - Character Assets & Style Guide (Monkey Island)'; category = 'Style Guide'; }
  else if (num === 19) { title = 'Si Juki - Streetwear & Hustle Merchandise Line'; category = 'Merchandise'; }
  else if (num === 20) { title = 'Hai Dudu - Theme, Backstory & Whimsical Trio'; category = 'Hai Dudu'; }
  else if (num === 21) { title = 'Hai Dudu - Character Expressions & Style Guide'; category = 'Style Guide'; }
  else if (num === 22) { title = 'Hai Dudu - Pastel Merchandise & Accessory Line'; category = 'Merchandise'; }
  else if (num === 23) { title = 'Fun Cican - Theme, Ecosystem & 55 Storybooks'; category = 'Fun Cican'; }
  else if (num === 24) { title = 'Fun Cican - Character Pose Style Guide'; category = 'Style Guide'; }
  else if (num === 25) { title = 'Fun Cican - Kids Bags & Merch Collection'; category = 'Merchandise'; }
  else if (num === 26) { title = 'Kidbash - Redefining Heroism & Storyline'; category = 'Kidbash'; }
  else if (num === 27) { title = 'Kidbash - 3D Character Poses Style Guide'; category = 'Style Guide'; }
  else if (num === 28) { title = 'Kidbash - Retro Arcade Merchandise Collection'; category = 'Merchandise'; }
  else if (num === 29) { title = 'Bona & Friends - Theme, Friends & Bobo Magazine Legacy'; category = 'Bona & Friends'; }
  else if (num === 30) { title = 'Bona & Friends - Character Style Guide Roster'; category = 'Style Guide'; }
  else if (num === 34) { title = 'Expanded IP Portfolio: Panji, Dino, Unicorn, Bear Republic, Byeol'; category = 'Portfolio'; }
  else if (num === 35) { title = 'Contact Provaliant Studios & Business Partnership Info'; category = 'Contact'; }
  
  return {
    number: num,
    title: title,
    category: category,
    src: 'img/slide-' + String(num).padStart(2, '0') + '.jpg'
  };
});
window.hIPlayApp = {
  activeTab: 'all',
  currentModalIP: null,
  currentSlideIdx: 0,

  init() {
    this.renderIPGrid('all');
    this.renderSlideDeckThumbnails();
    this.setupSmoothScroll();
    this.setupIntersectionObserver();
  },

  setTab(tab) {
    this.activeTab = tab;
    document.querySelectorAll('.filter-btn').forEach(btn => {
      if (btn.dataset.tab === tab) {
        btn.className = 'filter-btn px-5 py-2.5 rounded-full text-xs md:text-sm font-bold transition-all duration-200 bg-slate-900 text-white shadow-md';
      } else {
        btn.className = 'filter-btn px-5 py-2.5 rounded-full text-xs md:text-sm font-bold transition-all duration-200 bg-white text-slate-600 hover:bg-slate-100 border border-slate-200';
      }
    });
    this.renderIPGrid(tab);
  },

  renderIPGrid(filter) {
    const container = document.getElementById('ipGridContainer');
    if (!container) return;

    let items = IP_DATABASE;
    if (filter === 'original') {
      items = IP_DATABASE.filter(item => item.type === 'original');
    } else if (filter === 'collab') {
      items = IP_DATABASE.filter(item => item.type === 'collab');
    } else if (filter === 'family') {
      items = IP_DATABASE.filter(item => ['panji', 'bona', 'fun-cican', 'dino-island'].includes(item.id));
    } else if (filter === 'pop') {
      items = IP_DATABASE.filter(item => ['si-juki', 'milk-mocha', 'hai-dudu', 'kidbash'].includes(item.id));
    }

    container.innerHTML = items.map(ip => `
      <div class="group bg-white rounded-3xl p-6 border border-slate-200/80 shadow-sm hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 flex flex-col justify-between relative overflow-hidden">
        <div class="absolute top-0 left-0 right-0 h-2" style="background: linear-gradient(90deg, ${ip.accentColor}, #FFA200, #00A8FF)"></div>
        <div>
          <div class="flex items-center justify-between gap-2 mb-4">
            <span class="px-3 py-1 text-xs font-bold rounded-full bg-slate-100 text-slate-800 border border-slate-200/60">
              ${ip.badge}
            </span>
            <span class="text-xs font-semibold text-slate-600 tracking-wide uppercase">
              ${ip.studio}
            </span>
          </div>

          <div class="relative w-full h-56 rounded-2xl overflow-hidden bg-slate-100 mb-5 border border-slate-100 cursor-pointer" onclick="hIPlayApp.openIPModal('${ip.id}')">
            <img src="${ip.coverImage}" alt="${ip.name}" class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-500 ease-out" />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/70 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-4">
              <span class="text-white text-xs font-bold flex items-center gap-1.5 bg-slate-900/80 px-3 py-1.5 rounded-full backdrop-blur-md">
                <i data-lucide="expand" class="w-3.5 h-3.5"></i> Explore IP Deep-Dive
              </span>
            </div>
          </div>

          <h3 class="text-2xl font-bold text-slate-900 mb-1.5 font-display flex items-center justify-between">
            <span>${ip.name}</span>
          </h3>
          <p class="text-xs font-bold uppercase tracking-wider text-rose-500 mb-2">${ip.categoryTag}</p>
          <p class="text-sm font-semibold text-slate-700 mb-3">${ip.tagline}</p>
          <p class="text-xs text-slate-500 line-clamp-3 leading-relaxed mb-6">${ip.summary}</p>
        </div>

        <div>
          <div class="grid grid-cols-3 gap-2 p-3 rounded-2xl bg-slate-50 border border-slate-100 mb-4 text-center">
            ${ip.metrics.map(m => `
              <div class="flex flex-col justify-center">
                <div class="text-[11px] font-extrabold text-slate-900 truncate">${m.val}</div>
                <div class="text-[9px] text-slate-400 font-medium">${m.label}</div>
              </div>
            `).join('')}
          </div>

          <div class="flex items-center gap-2">
            <button onclick="hIPlayApp.openIPModal('${ip.id}')" class="flex-1 py-2.5 px-4 rounded-xl bg-slate-900 hover:bg-rose-500 text-white text-xs font-bold transition-colors flex items-center justify-center gap-1.5 shadow-sm">
              <span>View Style Guide & Merch</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </button>
            <button onclick="hIPlayApp.openDeckModal(${ip.slides[0]})" class="p-2.5 rounded-xl border border-slate-200 text-slate-600 hover:bg-slate-100 transition-colors" title="View in Slide Deck">
              <i data-lucide="file-text" class="w-4 h-4"></i>
            </button>
          </div>
        </div>
      </div>
    `).join('');

    if (window.lucide) {
      lucide.createIcons();
    }
  },

  openIPModal(ipId) {
    const ip = IP_DATABASE.find(item => item.id === ipId);
    if (!ip) return;
    this.currentModalIP = ip;

    const modal = document.getElementById('ipDetailModal');
    const content = document.getElementById('ipDetailContent');
    if (!modal || !content) return;

    content.innerHTML = `
      <div class="p-6 md:p-10">
        <div class="flex flex-wrap items-start justify-between gap-4 pb-6 border-b border-slate-100">
          <div>
            <div class="flex items-center gap-2 mb-2">
              <span class="px-3 py-1 rounded-full text-xs font-bold bg-rose-100 text-rose-700">
                ${ip.badge}
              </span>
              <span class="text-xs font-semibold text-slate-500">
                ${ip.categoryTag}
              </span>
            </div>
            <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 font-display">${ip.name}</h2>
            <p class="text-base text-slate-600 font-medium mt-1">${ip.tagline}</p>
          </div>
          <button onclick="hIPlayApp.closeIPModal()" class="p-2.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 transition-colors">
            <i data-lucide="x" class="w-5 h-5"></i>
          </button>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 my-8">
          <div class="lg:col-span-5 space-y-6">
            <div class="p-5 rounded-2xl bg-gradient-to-br from-slate-50 to-slate-100/70 border border-slate-200/60">
              <h4 class="text-xs font-bold uppercase tracking-wider text-slate-500 mb-3 flex items-center gap-2">
                <i data-lucide="book-open" class="w-4 h-4 text-rose-500"></i> Theme & Narrative
              </h4>
              <p class="text-sm text-slate-700 leading-relaxed">${ip.theme}</p>
            </div>

            <div class="p-5 rounded-2xl bg-white border border-slate-200/80 shadow-sm">
              <h4 class="text-xs font-bold uppercase tracking-wider text-slate-500 mb-3 flex items-center gap-2">
                <i data-lucide="sparkles" class="w-4 h-4 text-amber-500"></i> Background & Community Reach
              </h4>
              <p class="text-sm text-slate-700 leading-relaxed">${ip.background}</p>
            </div>

            <div class="p-5 rounded-2xl bg-slate-900 text-white">
              <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-3">Key Highlights & Metrics</h4>
              <div class="grid grid-cols-1 gap-3">
                ${ip.metrics.map(m => `
                  <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                    <span class="text-xs text-slate-400">${m.label}</span>
                    <span class="text-sm font-bold text-amber-400">${m.val}</span>
                  </div>
                `).join('')}
              </div>
            </div>

            <div class="p-5 rounded-2xl bg-rose-50 border border-rose-100">
              <h4 class="text-xs font-bold uppercase tracking-wider text-rose-700 mb-2">Commercial Merch Line</h4>
              <ul class="text-xs text-slate-700 space-y-1.5">
                ${ip.merchHighlights ? ip.merchHighlights.map(h => `<li class="flex items-start gap-2"><i data-lucide="check-circle" class="w-3.5 h-3.5 text-rose-500 shrink-0 mt-0.5"></i> ${h}</li>`).join('') : ''}
              </ul>
            </div>
          </div>

          <div class="lg:col-span-7 space-y-6">
            ${ip.styleGuideImage ? `
              <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200">
                <div class="flex items-center justify-between mb-3">
                  <h4 class="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                    <i data-lucide="palette" class="w-4 h-4 text-blue-500"></i> Official Character Style Guide Preview
                  </h4>
                  <button onclick="hIPlayApp.openDeckModal(${ip.slides[1] || ip.slides[0]})" class="text-xs font-semibold text-rose-600 hover:underline">
                    View Full Slide ↗
                  </button>
                </div>
                <div class="rounded-xl overflow-hidden border border-slate-200 shadow-inner bg-white">
                  <img src="${ip.styleGuideImage}" alt="${ip.name} Style Guide" class="w-full h-auto object-contain" />
                </div>
              </div>
            ` : ''}

            ${ip.merchImage ? `
              <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200">
                <div class="flex items-center justify-between mb-3">
                  <h4 class="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                    <i data-lucide="shopping-bag" class="w-4 h-4 text-emerald-500"></i> Commercial Merchandise Mockups
                  </h4>
                  <button onclick="hIPlayApp.openDeckModal(${ip.slides[2] || ip.slides[0]})" class="text-xs font-semibold text-rose-600 hover:underline">
                    View Full Slide ↗
                  </button>
                </div>
                <div class="rounded-xl overflow-hidden border border-slate-200 shadow-inner bg-white">
                  <img src="${ip.merchImage}" alt="${ip.name} Merchandise" class="w-full h-auto object-contain" />
                </div>
              </div>
            ` : ''}

            ${ip.mascotImage ? `
              <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200">
                <div class="flex items-center justify-between mb-3">
                  <h4 class="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                    <i data-lucide="smile" class="w-4 h-4 text-amber-500"></i> Mascot Activation & Stage Appearance
                  </h4>
                  <button onclick="hIPlayApp.openDeckModal(${ip.slides[3] || 4})" class="text-xs font-semibold text-rose-600 hover:underline">
                    View Full Slide ↗
                  </button>
                </div>
                <div class="rounded-xl overflow-hidden border border-slate-200 shadow-inner bg-white">
                  <img src="${ip.mascotImage}" alt="${ip.name} Mascot" class="w-full h-auto object-contain" />
                </div>
              </div>
            ` : ''}
          </div>
        </div>

        <div class="pt-6 border-t border-slate-100 flex flex-wrap items-center justify-between gap-4">
          <div class="text-xs text-slate-500">
            Interested in licensing or hosting <strong>${ip.name}</strong> at your venue?
          </div>
          <div class="flex items-center gap-3">
            <a href="#contact" onclick="hIPlayApp.closeIPModal(); hIPlayApp.prefillInquiry('${ip.name}')" class="py-2.5 px-6 rounded-xl bg-gradient-to-r from-rose-500 to-amber-500 text-white text-xs font-bold shadow-md hover:opacity-90 transition-opacity">
              Inquire Licensing / Booking
            </a>
            <button onclick="hIPlayApp.closeIPModal()" class="py-2.5 px-5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold transition-colors">
              Close
            </button>
          </div>
        </div>
      </div>
    `;

    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden';

    if (window.lucide) {
      lucide.createIcons();
    }
  },

  closeIPModal() {
    const modal = document.getElementById('ipDetailModal');
    if (!modal) return;
    modal.classList.add('hidden');
    modal.classList.remove('flex');
    document.body.style.overflow = 'auto';
  },

  renderSlideDeckThumbnails() {
    const container = document.getElementById('deckThumbnailsContainer');
    if (!container) return;

    container.innerHTML = ALL_SLIDES.map((slide, idx) => `
      <div onclick="hIPlayApp.goToSlide(${idx})" class="group cursor-pointer rounded-xl overflow-hidden border-2 transition-all p-1 bg-white hover:border-rose-500 ${idx === this.currentSlideIdx ? 'border-rose-500 shadow-md ring-2 ring-rose-200' : 'border-slate-200'}" id="thumb-${idx}">
        <div class="aspect-video w-full rounded-lg overflow-hidden bg-slate-100 relative">
          <img src="${slide.src}" alt="${slide.title}" class="w-full h-full object-cover" loading="lazy" />
          <span class="absolute bottom-1 right-1 bg-slate-900/80 text-white text-[10px] font-bold px-1.5 py-0.5 rounded backdrop-blur-sm">
            #${slide.number}
          </span>
        </div>
        <div class="mt-1.5 px-1">
          <p class="text-[11px] font-semibold text-slate-800 truncate group-hover:text-rose-600">${slide.title}</p>
          <span class="text-[9px] text-slate-400 font-medium">${slide.category}</span>
        </div>
      </div>
    `).join('');
  },

  openDeckModal(slideNumber = 1) {
    this.currentSlideIdx = Math.max(0, Math.min(34, slideNumber - 1));
    const modal = document.getElementById('deckViewerModal');
    if (!modal) return;

    this.updateDeckViewerUI();
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden';
  },

  closeDeckModal() {
    const modal = document.getElementById('deckViewerModal');
    if (!modal) return;
    modal.classList.add('hidden');
    modal.classList.remove('flex');
    document.body.style.overflow = 'auto';
  },

  nextSlide() {
    if (this.currentSlideIdx < ALL_SLIDES.length - 1) {
      this.currentSlideIdx++;
      this.updateDeckViewerUI();
    }
  },

  prevSlide() {
    if (this.currentSlideIdx > 0) {
      this.currentSlideIdx--;
      this.updateDeckViewerUI();
    }
  },

  goToSlide(idx) {
    this.currentSlideIdx = idx;
    this.updateDeckViewerUI();
  },

  updateDeckViewerUI() {
    const slide = ALL_SLIDES[this.currentSlideIdx];
    if (!slide) return;

    const mainImg = document.getElementById('deckMainImage');
    const titleEl = document.getElementById('deckSlideTitle');
    const catEl = document.getElementById('deckSlideCategory');
    const numEl = document.getElementById('deckSlideNumber');
    const prevBtn = document.getElementById('deckPrevBtn');
    const nextBtn = document.getElementById('deckNextBtn');

    if (mainImg) mainImg.src = slide.src;
    if (titleEl) titleEl.textContent = slide.title;
    if (catEl) catEl.textContent = slide.category;
    if (numEl) numEl.textContent = 'Slide ' + slide.number + ' of ' + ALL_SLIDES.length;

    if (prevBtn) prevBtn.disabled = this.currentSlideIdx === 0;
    if (nextBtn) nextBtn.disabled = this.currentSlideIdx === ALL_SLIDES.length - 1;

    const activeThumb = document.getElementById('thumb-' + this.currentSlideIdx);
    if (activeThumb) {
      document.querySelectorAll('#deckThumbnailsContainer > div').forEach(el => {
        el.classList.remove('border-rose-500', 'ring-2', 'ring-rose-200');
        el.classList.add('border-slate-200');
      });
      activeThumb.classList.add('border-rose-500', 'ring-2', 'ring-rose-200');
      activeThumb.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    }
  },

  prefillInquiry(ipName) {
    const select = document.getElementById('inquiryIP');
    const message = document.getElementById('inquiryMessage');
    if (select) {
      for (let i = 0; i < select.options.length; i++) {
        if (select.options[i].text.includes(ipName) || select.options[i].value.includes(ipName.toLowerCase())) {
          select.selectedIndex = i;
          break;
        }
      }
    }
    if (message) {
      message.value = 'Hello Provaliant Studios team, we are interested in exploring partnership / licensing opportunities for ' + ipName + ' at our venue/event.';
    }
  },

  handleContactSubmit(event) {
    event.preventDefault();
    const name = document.getElementById('contactName')?.value || 'Partner';
    const company = document.getElementById('contactCompany')?.value || 'Organization';
    const email = document.getElementById('contactEmail')?.value || '';
    const phone = document.getElementById('contactPhone')?.value || '';
    const ipInterest = document.getElementById('inquiryIP')?.value || 'All IPs';
    const message = document.getElementById('inquiryMessage')?.value || '';

    const feedback = document.getElementById('contactFormFeedback');
    if (feedback) {
      feedback.innerHTML = `
        <div class="p-4 rounded-2xl bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs flex items-start gap-3">
          <i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-600 shrink-0"></i>
          <div>
            <strong class="font-bold block text-sm mb-0.5">Inquiry Sent Successfully!</strong>
            Thank you, ${name} from ${company}. Our partnerships team (Nungky Pratiwi & Chandra Sugiono) will reach out to you at ${email || phone} shortly.
          </div>
        </div>
      `;
      if (window.lucide) lucide.createIcons();
    }

    const mailto = 'mailto:nungky@provaliantgroup.com,chandra@provaliantgroup.com?subject=hIPlay Partnership Inquiry from ' + encodeURIComponent(company) + ' - ' + encodeURIComponent(name) + '&body=' + encodeURIComponent('Name: ' + name + '\\nCompany: ' + company + '\\nEmail: ' + email + '\\nPhone: ' + phone + '\\nIP of Interest: ' + ipInterest + '\\n\\nMessage:\\n' + message);
    
    setTimeout(() => {
      window.location.href = mailto;
    }, 1200);
  },

  setupSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#' || !href) return;
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  },

  setupIntersectionObserver() {
    window.addEventListener('keydown', (e) => {
      const modal = document.getElementById('deckViewerModal');
      if (modal && !modal.classList.contains('hidden')) {
        if (e.key === 'ArrowRight' || e.key === 'PageDown') {
          this.nextSlide();
        } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
          this.prevSlide();
        } else if (e.key === 'Escape') {
          this.closeDeckModal();
        }
      }
      const ipModal = document.getElementById('ipDetailModal');
      if (ipModal && !ipModal.classList.contains('hidden')) {
        if (e.key === 'Escape') {
          this.closeIPModal();
        }
      }
    });
  }
};

document.addEventListener('DOMContentLoaded', () => {
  window.hIPlayApp.init();
});
"""

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js_content)
print('app.js successfully built!')

index_html_content = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>hIPlay | Indonesia's Premier IP Playground & Experience Platform</title>
  <meta name="description" content="hIPlay is Indonesia's leading IP Experience Platform by Provaliant Studios. Bringing iconic characters into real-life events, merchandise, and global franchises." />
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            hiplay: {
              red: '#FF4D5A',
              coral: '#FF6B6B',
              yellow: '#FFB703',
              amber: '#FFA200',
              blue: '#00A8FF',
              cyan: '#0EA5E9',
              purple: '#8B5CF6',
              violet: '#6D28D9',
              green: '#10B981',
              pink: '#F472B6',
              dark: '#0F172A'
            }
          },
          fontFamily: {
            sans: ['Plus Jakarta Sans', 'sans-serif'],
            display: ['Fredoka', 'Plus Jakarta Sans', 'sans-serif']
          }
        }
      }
    }
  </script>
  
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  
  <!-- Custom Styles -->
  <link rel="stylesheet" href="styles.css" />
</head>
<body class="bg-[#FAFBFC] text-slate-900 selection:bg-rose-500 selection:text-white font-sans antialiased relative">

  <!-- Floating Candy Ambient Glows -->
  <div class="bubble-shape bubble-yellow w-[500px] h-[500px] -top-32 -left-32"></div>
  <div class="bubble-shape bubble-coral w-[600px] h-[600px] top-40 -right-40"></div>
  <div class="bubble-shape bubble-blue w-[500px] h-[500px] top-[1400px] -left-20"></div>
  <div class="bubble-shape bubble-purple w-[600px] h-[600px] top-[2600px] -right-32"></div>

  <!-- Announcement Bar -->
  <div class="bg-gradient-to-r from-rose-500 via-amber-500 to-sky-500 text-white text-xs font-bold py-2 px-4 text-center sticky top-0 z-50 shadow-sm flex items-center justify-center gap-2">
    <span>🇮🇩 Endorsed by Ministry of Creative Economy of Indonesia • First Ever City Host Initiative</span>
    <button onclick="hIPlayApp.openDeckModal(1)" class="hidden md:inline-flex items-center gap-1 bg-white/20 hover:bg-white/30 px-2.5 py-0.5 rounded-full backdrop-blur-md transition-colors text-[11px]">
      <span>View Deck</span> <i data-lucide="arrow-up-right" class="w-3 h-3"></i>
    </button>
  </div>

  <!-- Sticky Glass Navigation -->
  <header class="sticky top-8 z-40 glass-nav transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      
      <!-- Brand Logo -->
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
      </a>

      <!-- Desktop Nav Links -->
      <nav class="hidden lg:flex items-center gap-7 text-xs font-bold text-slate-600">
        <a href="#about" class="hover:text-rose-500 transition-colors">The Vision</a>
        <a href="#engine" class="hover:text-rose-500 transition-colors">Platform Engine</a>
        <a href="#featured-ips" class="hover:text-rose-500 transition-colors">IP Universe</a>
        <a href="#mascots" class="hover:text-rose-500 transition-colors">Live Mascots</a>
        <a href="#services" class="hover:text-rose-500 transition-colors">Services</a>
        <a href="#merchandise" class="hover:text-rose-500 transition-colors">Merchandise</a>
        <a href="#deck-viewer" class="hover:text-rose-500 transition-colors">Deck Explorer</a>
        <a href="#contact" class="hover:text-rose-500 transition-colors">Contact</a>
      </nav>

      <!-- Action Buttons -->
      <div class="flex items-center gap-3">
        <button onclick="hIPlayApp.openDeckModal(1)" class="hidden sm:inline-flex items-center gap-1.5 py-2.5 px-4 rounded-xl border border-slate-200 text-slate-700 hover:bg-slate-50 text-xs font-bold transition-all shadow-sm">
          <i data-lucide="presentation" class="w-4 h-4 text-slate-500"></i>
          <span>Deck (35 Slides)</span>
        </button>
        <a href="#contact" class="inline-flex items-center gap-2 py-2.5 px-5 rounded-xl bg-slate-900 hover:bg-rose-500 text-white text-xs font-bold transition-all shadow-md hover:shadow-lg">
          <span>Partner With Us</span>
          <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
        </a>
      </div>

    </div>
  </header>

  <!-- Hero Section -->
  <section class="relative pt-12 pb-20 md:pt-20 md:pb-28 overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Top Pill -->
      <div class="inline-flex items-center gap-2.5 px-4 py-2 rounded-full gradient-hero-badge shadow-sm mb-6 animate-float">
        <span class="w-2 h-2 rounded-full bg-rose-500 animate-ping"></span>
        <span class="text-xs font-extrabold text-slate-800 tracking-wide">
          🌟 Indonesia's IP Experience Platform Bringing Characters into Real Life
        </span>
      </div>

      <!-- Main Headline -->
      <div class="max-w-4xl">
        <h1 class="text-4xl sm:text-6xl lg:text-7xl font-extrabold text-slate-900 tracking-tight leading-[1.1] mb-6">
          Transforming Indonesian IPs into <br class="hidden sm:inline" />
          <span class="gradient-hiplay-text font-display">Real-World Magic</span> & Global Franchises.
        </h1>
        <p class="text-lg sm:text-xl text-slate-600 font-medium leading-relaxed mb-8 max-w-3xl">
          <strong class="text-slate-900">hIPlay is not just a playground.</strong> It is a comprehensive IP Experience Platform that transforms beloved characters into unforgettable live events, vibrant fan communities, and high-growth commercial ecosystems.
        </p>

        <!-- CTA Action Group -->
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
        </div>
      </div>

      <!-- Character Floating Chips Banner -->
      <div class="bg-white/80 backdrop-blur-xl rounded-3xl p-6 sm:p-8 border border-slate-200/80 shadow-xl mb-14">
        <div class="flex flex-wrap items-center justify-between gap-4 mb-5 pb-4 border-b border-slate-100">
          <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
            <span class="text-xs font-extrabold uppercase tracking-widest text-slate-400">Featured IP Roster</span>
          </div>
          <span class="text-xs font-bold text-slate-600">Click any character to jump into their story & style guide</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3">
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
            <span class="text-xs font-bold text-slate-800 block truncate group-hover:text-pink-700">Bona & Friends</span>
            <span class="text-[10px] text-pink-600 font-semibold">Bobo Heritage</span>
          </div>
        </div>
      </div>

      <!-- Stats Bar -->
      <div class="grid grid-cols-2 md:grid-cols-5 gap-4">
        <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-sm text-center">
          <div class="text-3xl font-extrabold text-slate-900 font-display">8+</div>
          <div class="text-xs text-slate-500 font-medium mt-1">Leading IP Franchises</div>
        </div>
        <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-sm text-center">
          <div class="text-3xl font-extrabold text-rose-500 font-display">1M+</div>
          <div class="text-xs text-slate-500 font-medium mt-1">Global Social Following</div>
        </div>
        <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-sm text-center">
          <div class="text-3xl font-extrabold text-amber-500 font-display">14.0%</div>
          <div class="text-xs text-slate-500 font-medium mt-1">Viral Engagement Rate</div>
        </div>
        <div class="bg-white p-5 rounded-2xl border border-slate-200/80 shadow-sm text-center">
          <div class="text-3xl font-extrabold text-sky-500 font-display">55+</div>
          <div class="text-xs text-slate-500 font-medium mt-1">Storybooks Published</div>
        </div>
        <div class="col-span-2 md:col-span-1 bg-white p-5 rounded-2xl border border-slate-200/80 shadow-sm text-center">
          <div class="text-2xl font-extrabold text-purple-600 font-display">UNESCO</div>
          <div class="text-xs text-slate-500 font-medium mt-1">Heritage Lore Reimagined</div>
        </div>
      </div>

    </div>
  </section>

  <!-- Platform Engine / Flywheel Section -->
  <section id="engine" class="py-20 bg-white border-y border-slate-200/80 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="px-3.5 py-1.5 rounded-full text-xs font-extrabold uppercase tracking-wider bg-rose-100 text-rose-700 mb-3 inline-block">
          The 5-Stage IP Flywheel
        </span>
        <h2 class="text-3xl sm:text-5xl font-extrabold text-slate-900 font-display tracking-tight mt-2">
          From Live Event to Exponential IP Growth
        </h2>
        <p class="text-slate-600 font-medium text-base mt-4">
          How hIPlay transforms character stories into sustainable commercial ecosystems through physical and digital touchpoints.
        </p>
      </div>

      <!-- Flywheel Cards Grid -->
      <div class="grid grid-cols-1 md:grid-cols-5 gap-4 relative">
        
        <!-- Step 1 -->
        <div class="gradient-funnel-card p-6 rounded-3xl border border-slate-200/80 flex flex-col justify-between hover:border-rose-400 transition-all group">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-rose-500/10 text-rose-600 flex items-center justify-center font-black text-lg mb-4 group-hover:scale-110 transition-transform">
              01
            </div>
            <h3 class="text-lg font-bold text-slate-900 font-display mb-2">Event</h3>
            <p class="text-xs text-slate-500 leading-relaxed">
              City host activations, touring character roadshows, festivals, and venue takeovers that generate massive initial excitement.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-xs font-semibold text-rose-500">
            <span>Stage 1</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </div>
        </div>

        <!-- Step 2 -->
        <div class="gradient-funnel-card p-6 rounded-3xl border border-slate-200/80 flex flex-col justify-between hover:border-amber-400 transition-all group">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-amber-500/10 text-amber-600 flex items-center justify-center font-black text-lg mb-4 group-hover:scale-110 transition-transform">
              02
            </div>
            <h3 class="text-lg font-bold text-slate-900 font-display mb-2">Experience</h3>
            <p class="text-xs text-slate-500 leading-relaxed">
              Immersive thematic playgrounds, interactive mascot shows, games, and photo moments that forge deep emotional connections.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-xs font-semibold text-amber-500">
            <span>Stage 2</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </div>
        </div>

        <!-- Step 3 -->
        <div class="gradient-funnel-card p-6 rounded-3xl border border-slate-200/80 flex flex-col justify-between hover:border-sky-400 transition-all group">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-sky-500/10 text-sky-600 flex items-center justify-center font-black text-lg mb-4 group-hover:scale-110 transition-transform">
              03
            </div>
            <h3 class="text-lg font-bold text-slate-900 font-display mb-2">Community</h3>
            <p class="text-xs text-slate-500 leading-relaxed">
              Viral social media fandoms, UGC content, active follower discussions, and multi-generational family loyalty.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-xs font-semibold text-sky-500">
            <span>Stage 3</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </div>
        </div>

        <!-- Step 4 -->
        <div class="gradient-funnel-card p-6 rounded-3xl border border-slate-200/80 flex flex-col justify-between hover:border-purple-400 transition-all group">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-purple-500/10 text-purple-600 flex items-center justify-center font-black text-lg mb-4 group-hover:scale-110 transition-transform">
              04
            </div>
            <h3 class="text-lg font-bold text-slate-900 font-display mb-2">Monetization</h3>
            <p class="text-xs text-slate-500 leading-relaxed">
              Licensed retail merchandise, ticketing, limited edition drops, brand sponsorships, and master licensing agreements.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-xs font-semibold text-purple-500">
            <span>Stage 4</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </div>
        </div>

        <!-- Step 5 -->
        <div class="gradient-funnel-card p-6 rounded-3xl border border-slate-200/80 flex flex-col justify-between hover:border-emerald-400 transition-all group">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-emerald-500/10 text-emerald-600 flex items-center justify-center font-black text-lg mb-4 group-hover:scale-110 transition-transform">
              05
            </div>
            <h3 class="text-lg font-bold text-slate-900 font-display mb-2">IP Growth</h3>
            <p class="text-xs text-slate-500 leading-relaxed">
              Expanding franchises into animated feature films, series, interactive video games, and international exports.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-xs font-semibold text-emerald-500">
            <span>Stage 5</span>
            <i data-lucide="repeat" class="w-4 h-4"></i>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- Section: National Mission & Creative Economy -->
  <section id="about" class="py-20 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <div class="lg:col-span-6 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-extrabold uppercase tracking-wider bg-amber-100 text-amber-800">
            <i data-lucide="award" class="w-4 h-4 text-amber-600"></i>
            <span>Government Endorsed Initiative</span>
          </div>

          <h2 class="text-3xl sm:text-5xl font-extrabold text-slate-900 font-display tracking-tight leading-tight">
            Inviting You to Join Our Mission to Boost <br />
            <span class="gradient-hiplay-text">Indonesia's Creative Economy!</span>
          </h2>

          <p class="text-base text-slate-600 leading-relaxed">
            <strong>hIPlay is set to be the trailblazing initiative that catapults the Creative Economy into action</strong>, all with your valuable support as the first ever city host and the official endorsement from the <strong>Ministry of Creative Economy of Indonesia</strong>.
          </p>

          <div class="space-y-4 pt-2">
            <div class="flex items-start gap-4 p-4 rounded-2xl bg-white border border-slate-200/80 shadow-sm">
              <div class="w-10 h-10 rounded-xl bg-rose-100 text-rose-600 flex items-center justify-center shrink-0">
                <i data-lucide="map-pin" class="w-5 h-5"></i>
              </div>
              <div>
                <h4 class="text-sm font-bold text-slate-900">Pioneering City Host Initiative</h4>
                <p class="text-xs text-slate-500 mt-0.5">Empowering Indonesian cities and regional venues to host premier pop culture IP playgrounds.</p>
              </div>
            </div>

            <div class="flex items-start gap-4 p-4 rounded-2xl bg-white border border-slate-200/80 shadow-sm">
              <div class="w-10 h-10 rounded-xl bg-sky-100 text-sky-600 flex items-center justify-center shrink-0">
                <i data-lucide="users" class="w-5 h-5"></i>
              </div>
              <div>
                <h4 class="text-sm font-bold text-slate-900">Uniting Diverse Audience Behaviors</h4>
                <p class="text-xs text-slate-500 mt-0.5">Combining distinct fan segments from kids and families to youth subcultures and retro gamers.</p>
              </div>
            </div>

            <div class="flex items-start gap-4 p-4 rounded-2xl bg-white border border-slate-200/80 shadow-sm">
              <div class="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-600 flex items-center justify-center shrink-0">
                <i data-lucide="trending-up" class="w-5 h-5"></i>
              </div>
              <div>
                <h4 class="text-sm font-bold text-slate-900">From Vision to Commerce</h4>
                <p class="text-xs text-slate-500 mt-0.5">Provaliant Studios acts as the creative and commercial bridge for long-term IP sustainability.</p>
              </div>
            </div>
          </div>

          <div class="pt-4 flex items-center gap-4">
            <a href="#contact" class="py-3 px-6 rounded-xl bg-slate-900 hover:bg-rose-500 text-white text-xs font-bold transition-colors">
              Host hIPlay in Your City
            </a>
            <button onclick="hIPlayApp.openDeckModal(2)" class="text-xs font-bold text-rose-600 hover:underline flex items-center gap-1">
              <span>View Slide 2 Details</span> <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </button>
          </div>

        </div>

        <div class="lg:col-span-6">
          <div class="relative rounded-3xl overflow-hidden shadow-2xl border-4 border-white bg-slate-100 group">
            <img src="img/Untitled copy_page-0002.jpg" alt="Mission Slide" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-500" />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/60 via-transparent to-transparent flex items-end p-6">
              <div class="text-white">
                <span class="text-[10px] font-bold uppercase tracking-wider text-amber-300">National Vision</span>
                <h4 class="text-base font-bold">Endorsed by Ministry of Creative Economy of Indonesia</h4>
              </div>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- Section: Featured IP Showcase & Filterable Hub -->
  <section id="featured-ips" class="py-20 bg-slate-50 border-t border-slate-200/80 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section Header -->
      <div class="flex flex-wrap items-end justify-between gap-6 mb-12">
        <div>
          <span class="px-3.5 py-1.5 rounded-full text-xs font-extrabold uppercase tracking-wider bg-sky-100 text-sky-800 mb-3 inline-block">
            IP Universe
          </span>
          <h2 class="text-3xl sm:text-5xl font-extrabold text-slate-900 font-display tracking-tight mt-2">
            Featured IPs & Audience Spectrum
          </h2>
          <p class="text-slate-600 font-medium text-sm sm:text-base mt-2 max-w-2xl">
            Each IP brings its own distinct audience segment. Combining different audience behaviors creates broader and deeper engagement across generations.
          </p>
        </div>

        <!-- Filter Tabs -->
        <div class="flex flex-wrap items-center gap-2 p-1.5 rounded-2xl bg-slate-200/70 border border-slate-300/60">
          <button onclick="hIPlayApp.setTab('all')" data-tab="all" class="filter-btn px-5 py-2.5 rounded-full text-xs md:text-sm font-bold transition-all duration-200 bg-slate-900 text-white shadow-md">
            ✨ All Franchises (8)
          </button>
          <button onclick="hIPlayApp.setTab('original')" data-tab="original" class="filter-btn px-5 py-2.5 rounded-full text-xs md:text-sm font-bold transition-all duration-200 bg-white text-slate-600 hover:bg-slate-100 border border-slate-200">
            🌟 Original IPs (Provaliant)
          </button>
          <button onclick="hIPlayApp.setTab('collab')" data-tab="collab" class="filter-btn px-5 py-2.5 rounded-full text-xs md:text-sm font-bold transition-all duration-200 bg-white text-slate-600 hover:bg-slate-100 border border-slate-200">
            🤝 Iconic Collaborations
          </button>
          <button onclick="hIPlayApp.setTab('family')" data-tab="family" class="filter-btn px-5 py-2.5 rounded-full text-xs md:text-sm font-bold transition-all duration-200 bg-white text-slate-600 hover:bg-slate-100 border border-slate-200">
            🧸 Kids & Family
          </button>
          <button onclick="hIPlayApp.setTab('pop')" data-tab="pop" class="filter-btn px-5 py-2.5 rounded-full text-xs md:text-sm font-bold transition-all duration-200 bg-white text-slate-600 hover:bg-slate-100 border border-slate-200">
            ⚡ Pop Culture & Youth
          </button>
        </div>
      </div>

      <!-- IP Grid Container (Populated by JS) -->
      <div id="ipGridContainer" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <!-- Javascript renders IP cards here -->
      </div>

    </div>
  </section>

  <!-- Mascot Real-Life Activations -->
  <section id="mascots" class="py-20 bg-white border-t border-slate-200/80 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="px-3.5 py-1.5 rounded-full text-xs font-extrabold uppercase tracking-wider bg-amber-100 text-amber-800 mb-3 inline-block">
          Real Life Experience
        </span>
        <h2 class="text-3xl sm:text-5xl font-extrabold text-slate-900 font-display tracking-tight mt-2">
          Character Mascot Costumes & Live Stage Magic
        </h2>
        <p class="text-slate-600 font-medium text-base mt-3">
          Bringing characters out of digital screens into real-world hugs, stage performances, and viral fan moments.
        </p>
      </div>

      <!-- Mascot Showcase Grid with Real Photos -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-12 items-center">
        
        <div class="lg:col-span-7">
          <div class="relative rounded-3xl overflow-hidden shadow-2xl border-4 border-white group">
            <img src="img/Untitled copy_page-0004.jpg" alt="Mascot Costumes Roster" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-500" />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/70 via-transparent to-transparent flex items-end p-6">
              <span class="text-white text-xs font-bold bg-slate-900/80 px-3 py-1.5 rounded-full backdrop-blur-md">
                Featured Character Mascot Costumes on Live Tour
              </span>
            </div>
          </div>
        </div>

        <div class="lg:col-span-5">
          <div class="relative rounded-3xl overflow-hidden shadow-2xl border-4 border-white group">
            <img src="img/Untitled copy_page-0009.jpg" alt="Legenda Panji Mascot Activation" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-500" />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/70 via-transparent to-transparent flex items-end p-6">
              <span class="text-white text-xs font-bold bg-rose-600/90 px-3 py-1.5 rounded-full backdrop-blur-md">
                Legenda Panji Live Stage Mascot Activation
              </span>
            </div>
          </div>
        </div>

      </div>

      <!-- 4 Experiential Pillars -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <div class="p-6 rounded-3xl bg-slate-50 border border-slate-200/80">
          <div class="w-12 h-12 rounded-2xl bg-rose-100 text-rose-600 flex items-center justify-center mb-4">
            <i data-lucide="sparkles" class="w-6 h-6"></i>
          </div>
          <h4 class="text-base font-bold text-slate-900 mb-2">Theatrical Stage Shows</h4>
          <p class="text-xs text-slate-500 leading-relaxed">
            Captivating live choreographed performances bringing stories to life with music and visual effects.
          </p>
        </div>

        <div class="p-6 rounded-3xl bg-slate-50 border border-slate-200/80">
          <div class="w-12 h-12 rounded-2xl bg-amber-100 text-amber-600 flex items-center justify-center mb-4">
            <i data-lucide="camera" class="w-6 h-6"></i>
          </div>
          <h4 class="text-base font-bold text-slate-900 mb-2">Meet & Greet Parades</h4>
          <p class="text-xs text-slate-500 leading-relaxed">
            Memorable photo opportunities and fan interaction that drives organic viral social shares.
          </p>
        </div>

        <div class="p-6 rounded-3xl bg-slate-50 border border-slate-200/80">
          <div class="w-12 h-12 rounded-2xl bg-sky-100 text-sky-600 flex items-center justify-center mb-4">
            <i data-lucide="layout-grid" class="w-6 h-6"></i>
          </div>
          <h4 class="text-base font-bold text-slate-900 mb-2">Mall & Venue Pop-Ups</h4>
          <p class="text-xs text-slate-500 leading-relaxed">
            Turn-key modular IP themed playgrounds, games, and merchandise booths boosting venue footfall.
          </p>
        </div>

        <div class="p-6 rounded-3xl bg-slate-50 border border-slate-200/80">
          <div class="w-12 h-12 rounded-2xl bg-purple-100 text-purple-600 flex items-center justify-center mb-4">
            <i data-lucide="globe-2" class="w-6 h-6"></i>
          </div>
          <h4 class="text-base font-bold text-slate-900 mb-2">City-Wide IP Tours</h4>
          <p class="text-xs text-slate-500 leading-relaxed">
            Scalable touring infrastructure allowing multi-city festivals across Indonesia and Southeast Asia.
          </p>
        </div>

      </div>

    </div>
  </section>

  <!-- Provaliant Studios & Business Solutions -->
  <section id="services" class="py-20 bg-slate-900 text-white relative overflow-hidden">
    <div class="bubble-shape bubble-blue w-[400px] h-[400px] top-0 right-0 opacity-20"></div>
    <div class="bubble-shape bubble-coral w-[500px] h-[500px] bottom-0 left-0 opacity-20"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center mb-16">
        <div class="lg:col-span-7">
          <span class="px-3.5 py-1.5 rounded-full text-xs font-extrabold uppercase tracking-wider bg-rose-500/20 text-rose-400 border border-rose-500/30 mb-3 inline-block">
            About Provaliant Studios
          </span>
          <h2 class="text-3xl sm:text-5xl font-extrabold text-white font-display tracking-tight mt-2 leading-tight">
            Elevating Your IP From <br />
            <span class="text-rose-400">Vision to Commerce.</span>
          </h2>
          <p class="text-slate-300 text-base mt-4 leading-relaxed max-w-2xl">
            As the heart of <strong>PROVALIANT GROUP</strong>, Provaliant Studios is Indonesia's leading Intellectual Property (IP) Studio, specializing in <strong>creation, development, and commercialization</strong> of original entertainment franchises for a global audience.
          </p>
          <div class="p-4 rounded-2xl bg-white/5 border border-white/10 mt-6 max-w-2xl">
            <p class="text-amber-300 text-sm font-semibold italic">
              "Our proposed value is simple: We build the universe; our partners help us bring it to the screen."
            </p>
          </div>
        </div>

        <div class="lg:col-span-5">
          <div class="p-6 rounded-3xl bg-white/10 backdrop-blur-xl border border-white/15">
            <h4 class="text-xs font-bold uppercase tracking-widest text-slate-400 mb-4">Provaliant Studio Engine</h4>
            <div class="flex items-center justify-around py-4">
              <div class="text-center">
                <div class="w-14 h-14 rounded-2xl bg-sky-500/20 text-sky-400 flex items-center justify-center font-bold text-sm mx-auto mb-2 border border-sky-500/30">
                  Creation
                </div>
                <span class="text-[11px] text-slate-300 font-medium">Worldbuilding</span>
              </div>
              <i data-lucide="arrow-right" class="w-5 h-5 text-slate-500"></i>
              <div class="text-center">
                <div class="w-14 h-14 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-sm mx-auto mb-2 border border-emerald-500/30">
                  Dev
                </div>
                <span class="text-[11px] text-slate-300 font-medium">Transmedia</span>
              </div>
              <i data-lucide="arrow-right" class="w-5 h-5 text-slate-500"></i>
              <div class="text-center">
                <div class="w-14 h-14 rounded-2xl bg-purple-500/20 text-purple-400 flex items-center justify-center font-bold text-sm mx-auto mb-2 border border-purple-500/30">
                  Monetize
                </div>
                <span class="text-[11px] text-slate-300 font-medium">Licensing</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 3 Core Services -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">
        
        <div class="p-8 rounded-3xl bg-slate-800/80 border border-slate-700/80 flex flex-col justify-between hover:border-rose-500/60 transition-all">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-rose-500/20 text-rose-400 flex items-center justify-center mb-6">
              <i data-lucide="trending-up" class="w-6 h-6"></i>
            </div>
            <h3 class="text-xl font-bold text-white mb-3">Developing & Expanding IPs</h3>
            <p class="text-xs text-slate-400 leading-relaxed">
              Focusing on commercially viable opportunities with a long-term perspective, scaling characters from concepts into expansive global franchises.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-700/60 text-xs text-rose-400 font-bold flex items-center gap-1">
            <span>Commercial Strategy</span> <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
          </div>
        </div>

        <div class="p-8 rounded-3xl bg-slate-800/80 border border-slate-700/80 flex flex-col justify-between hover:border-amber-500/60 transition-all">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center mb-6">
              <i data-lucide="shield-check" class="w-6 h-6"></i>
            </div>
            <h3 class="text-xl font-bold text-white mb-3">Managing Existing Local IPs</h3>
            <p class="text-xs text-slate-400 leading-relaxed">
              Overseeing events, merchandise manufacturing, brand collaborations, master licensing agreements, and IP rights protection.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-700/60 text-xs text-amber-400 font-bold flex items-center gap-1">
            <span>Master Licensing</span> <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
          </div>
        </div>

        <div class="p-8 rounded-3xl bg-slate-800/80 border border-slate-700/80 flex flex-col justify-between hover:border-sky-500/60 transition-all">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-sky-500/20 text-sky-400 flex items-center justify-center mb-6">
              <i data-lucide="film" class="w-6 h-6"></i>
            </div>
            <h3 class="text-xl font-bold text-white mb-3">Multimedia Production</h3>
            <p class="text-xs text-slate-400 leading-relaxed">
              Producing multimedia content utilizing technological advancements, emphasizing innovative approaches from OTT animations to gaming.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-700/60 text-xs text-sky-400 font-bold flex items-center gap-1">
            <span>Animation & Content</span> <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
          </div>
        </div>

      </div>

      <!-- Extended IP Portfolio Grid -->
      <div class="p-8 rounded-3xl bg-slate-800/40 border border-slate-700/80">
        <div class="flex flex-wrap items-center justify-between gap-4 mb-6">
          <div>
            <h4 class="text-lg font-bold text-white">Expanded Original Portfolio</h4>
            <p class="text-xs text-slate-400">Discover additional original IP worlds originating from Provaliant Studios.</p>
          </div>
          <button onclick="hIPlayApp.openDeckModal(34)" class="text-xs font-bold text-rose-400 hover:underline flex items-center gap-1">
            <span>View Slide 34 Matrix ↗</span>
          </button>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
          <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800">
            <span class="text-xl block mb-1">⚔️</span>
            <h5 class="text-xs font-bold text-white">Legenda Panji</h5>
            <p class="text-[10px] text-slate-400 mt-1">UNESCO Recognized Family Fantasy universe.</p>
          </div>
          <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800">
            <span class="text-xl block mb-1">🦖</span>
            <h5 class="text-xs font-bold text-white">Dino Island</h5>
            <p class="text-[10px] text-slate-400 mt-1">Educational dinosaur adventures with Diby Dino Baby.</p>
          </div>
          <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800">
            <span class="text-xl block mb-1">🦄</span>
            <h5 class="text-xs font-bold text-white">Magical Unicorn</h5>
            <p class="text-[10px] text-slate-400 mt-1">Fantasy unicorns fighting against the dark fairy.</p>
          </div>
          <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800">
            <span class="text-xl block mb-1">🐻⚙️</span>
            <h5 class="text-xs font-bold text-white">Bear Republic</h5>
            <p class="text-[10px] text-slate-400 mt-1">Steampunk bears, live RPG & slice-of-life adventures.</p>
          </div>
          <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800">
            <span class="text-xl block mb-1">🐹⭐</span>
            <h5 class="text-xs font-bold text-white">Byeol Star</h5>
            <p class="text-[10px] text-slate-400 mt-1">Alien hamster discovering Earth via K-Culture trends.</p>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- Commercial Merchandise Studio Showcase -->
  <section id="merchandise" class="py-20 bg-slate-50 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="px-3.5 py-1.5 rounded-full text-xs font-extrabold uppercase tracking-wider bg-emerald-100 text-emerald-800 mb-3 inline-block">
          Merchandising Engine
        </span>
        <h2 class="text-3xl sm:text-5xl font-extrabold text-slate-900 font-display tracking-tight mt-2">
          From Concept to Retail Ready
        </h2>
        <p class="text-slate-600 font-medium text-base mt-3">
          High-margin, quality-crafted merchandise lines tailored for every character demographic.
        </p>
      </div>

      <!-- Merchandise Preview Cards -->
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

      </div>

    </div>
  </section>

  <!-- Interactive Slide Deck Viewer Section -->
  <section id="deck-viewer" class="py-20 bg-white border-t border-slate-200/80 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-wrap items-end justify-between gap-6 mb-10">
        <div>
          <span class="px-3.5 py-1.5 rounded-full text-xs font-extrabold uppercase tracking-wider bg-rose-100 text-rose-800 mb-3 inline-block">
            Official Presentation Deck
          </span>
          <h2 class="text-3xl sm:text-5xl font-extrabold text-slate-900 font-display tracking-tight mt-2">
            Interactive Slide Deck Explorer
          </h2>
          <p class="text-slate-600 font-medium text-sm sm:text-base mt-2">
            Browse through all 35 official slides of the hIPlay & Provaliant Studios presentation in high resolution.
          </p>
        </div>

        <button onclick="hIPlayApp.openDeckModal(1)" class="py-3 px-6 rounded-xl bg-slate-900 hover:bg-rose-500 text-white text-xs font-bold transition-all shadow-md flex items-center gap-2">
          <i data-lucide="maximize-2" class="w-4 h-4"></i>
          <span>Open Fullscreen Deck Viewer</span>
        </button>
      </div>

      <!-- Thumbnail Strip Gallery -->
      <div id="deckThumbnailsContainer" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 lg:grid-cols-7 gap-3 max-h-[520px] overflow-y-auto p-4 rounded-3xl bg-slate-50 border border-slate-200/80 shadow-inner">
        <!-- Javascript renders 35 thumbnails here -->
      </div>

    </div>
  </section>

  <!-- Partnership & Contact Hub Section -->
  <section id="contact" class="py-20 bg-gradient-to-b from-slate-50 to-rose-50/40 border-t border-slate-200/80 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="px-3.5 py-1.5 rounded-full text-xs font-extrabold uppercase tracking-wider bg-rose-100 text-rose-800 mb-3 inline-block">
          Get in Touch
        </span>
        <h2 class="text-3xl sm:text-5xl font-extrabold text-slate-900 font-display tracking-tight mt-2">
          Partner as a City Host or License an IP
        </h2>
        <p class="text-slate-600 font-medium text-base mt-3">
          Reach out to our leadership team directly to explore licensing opportunities, venue hosting, or brand activations.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
        
        <!-- Left: Direct Contact Executive Cards -->
        <div class="lg:col-span-5 space-y-6">
          
          <!-- Nungky Card -->
          <div class="p-6 rounded-3xl bg-white border border-slate-200/80 shadow-sm hover:shadow-md transition-all">
            <div class="flex items-center gap-4 mb-4">
              <div class="w-14 h-14 rounded-2xl bg-rose-100 text-rose-600 flex items-center justify-center font-bold text-xl font-display">
                NP
              </div>
              <div>
                <h4 class="text-lg font-bold text-slate-900">Nungky Pratiwi</h4>
                <p class="text-xs text-slate-500 font-medium">GM Sales & Marketing • Provaliant Group</p>
              </div>
            </div>
            <div class="space-y-2 pt-2 border-t border-slate-100 text-xs">
              <a href="tel:+628158777447" class="flex items-center gap-2.5 text-slate-700 hover:text-rose-600 transition-colors font-medium">
                <i data-lucide="phone" class="w-4 h-4 text-slate-400"></i> +62 815-8777-447
              </a>
              <a href="mailto:nungky@provaliantgroup.com" class="flex items-center gap-2.5 text-slate-700 hover:text-rose-600 transition-colors font-medium">
                <i data-lucide="mail" class="w-4 h-4 text-slate-400"></i> nungky@provaliantgroup.com
              </a>
            </div>
            <div class="mt-4 pt-3 flex gap-2">
              <a href="https://wa.me/628158777447?text=Hello%20Nungky,%20I%20would%20like%20to%20inquire%20about%20hIPlay%20partnerships." target="_blank" class="flex-1 py-2 px-3 rounded-xl bg-emerald-500 hover:bg-emerald-600 text-white text-xs font-bold text-center transition-colors flex items-center justify-center gap-1.5">
                <i data-lucide="message-circle" class="w-3.5 h-3.5"></i> WhatsApp
              </a>
              <a href="mailto:nungky@provaliantgroup.com?subject=hIPlay%20Partnership%20Inquiry" class="py-2 px-3 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold transition-colors">
                Email
              </a>
            </div>
          </div>

          <!-- Chandra Card -->
          <div class="p-6 rounded-3xl bg-white border border-slate-200/80 shadow-sm hover:shadow-md transition-all">
            <div class="flex items-center gap-4 mb-4">
              <div class="w-14 h-14 rounded-2xl bg-amber-100 text-amber-600 flex items-center justify-center font-bold text-xl font-display">
                CS
              </div>
              <div>
                <h4 class="text-lg font-bold text-slate-900">Chandra Sugiono</h4>
                <p class="text-xs text-slate-500 font-medium">Partnership & Commercial Lead</p>
              </div>
            </div>
            <div class="space-y-2 pt-2 border-t border-slate-100 text-xs">
              <a href="tel:+62811107594" class="flex items-center gap-2.5 text-slate-700 hover:text-amber-600 transition-colors font-medium">
                <i data-lucide="phone" class="w-4 h-4 text-slate-400"></i> +62 811-107-594
              </a>
              <a href="mailto:chandra@provaliantgroup.com" class="flex items-center gap-2.5 text-slate-700 hover:text-amber-600 transition-colors font-medium">
                <i data-lucide="mail" class="w-4 h-4 text-slate-400"></i> chandra@provaliantgroup.com
              </a>
            </div>
            <div class="mt-4 pt-3 flex gap-2">
              <a href="https://wa.me/62811107594?text=Hello%20Chandra,%20I%20would%20like%20to%20inquire%20about%20hIPlay%20partnerships." target="_blank" class="flex-1 py-2 px-3 rounded-xl bg-emerald-500 hover:bg-emerald-600 text-white text-xs font-bold text-center transition-colors flex items-center justify-center gap-1.5">
                <i data-lucide="message-circle" class="w-3.5 h-3.5"></i> WhatsApp
              </a>
              <a href="mailto:chandra@provaliantgroup.com?subject=hIPlay%20Partnership%20Inquiry" class="py-2 px-3 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold transition-colors">
                Email
              </a>
            </div>
          </div>

          <!-- HQ Info -->
          <div class="p-6 rounded-3xl bg-white border border-slate-200/80 shadow-sm text-xs text-slate-600 space-y-2">
            <h5 class="font-bold text-slate-900 text-sm flex items-center gap-2">
              <i data-lucide="building" class="w-4 h-4 text-rose-500"></i> Provaliant Group HQ
            </h5>
            <p>Ruko Business Park - Kebon Jeruk. Blok E1 No. 11 - 12, Jl. Meruya Ilir No. 88 (Jl. Lapangan Bola), Jakarta 11620</p>
            <p>Phone: <strong>+62 21 300 61 595</strong></p>
            <p>Web: <a href="https://www.provaliantgroup.com" target="_blank" class="text-rose-600 hover:underline">www.provaliantgroup.com</a></p>
          </div>

        </div>

        <!-- Right: Interactive Inquiry Form -->
        <div class="lg:col-span-7">
          <div class="bg-white p-8 sm:p-10 rounded-3xl border border-slate-200/80 shadow-xl">
            <h3 class="text-2xl font-bold text-slate-900 font-display mb-2">Send an Inquiry</h3>
            <p class="text-xs text-slate-500 mb-6">Complete the form below and our team will get in touch with licensing kits and presentation materials.</p>

            <form onsubmit="hIPlayApp.handleContactSubmit(event)" class="space-y-4">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs font-bold text-slate-700 mb-1">Your Name *</label>
                  <input id="contactName" type="text" required placeholder="e.g. Budi Santoso" class="w-full px-4 py-3 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-rose-500" />
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate-700 mb-1">Organization / Mall / Brand *</label>
                  <input id="contactCompany" type="text" required placeholder="e.g. Grand Indonesia / City Mall" class="w-full px-4 py-3 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-rose-500" />
                </div>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs font-bold text-slate-700 mb-1">Work Email *</label>
                  <input id="contactEmail" type="email" required placeholder="name@company.com" class="w-full px-4 py-3 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-rose-500" />
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate-700 mb-1">Phone / WhatsApp Number *</label>
                  <input id="contactPhone" type="tel" required placeholder="+62 812 3456 7890" class="w-full px-4 py-3 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-rose-500" />
                </div>
              </div>

              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1">IP of Primary Interest</label>
                <select id="inquiryIP" class="w-full px-4 py-3 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-rose-500">
                  <option value="All IPs">🌟 All Featured IPs (Comprehensive hIPlay Tour)</option>
                  <option value="Legenda Panji">Legenda Panji Universe (Original Flagship)</option>
                  <option value="Milk Mocha Bear">Milk Mocha Bear (Viral Romance & Lifestyle)</option>
                  <option value="Si Juki">Si Juki (Indonesia's #1 Pop Culture Icon)</option>
                  <option value="Hai Dudu">Hai Dudu (Feel-Good Friends)</option>
                  <option value="Fun Cican">Fun Cican (Early Childhood Edutainment)</option>
                  <option value="Kidbash">Kidbash (Retro Arcade Superhero)</option>
                  <option value="Dino Island">Dino Island (Prehistoric Adventure)</option>
                  <option value="Bona & Friends">Bona & Friends (Bobo Magazine Heritage)</option>
                </select>
              </div>

              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1">Partnership Objectives & Message</label>
                <textarea id="inquiryMessage" rows="3" placeholder="Tell us about your city, venue, timing, and collaboration goals..." class="w-full px-4 py-3 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-rose-500"></textarea>
              </div>

              <div id="contactFormFeedback"></div>

              <button type="submit" class="w-full py-4 px-6 rounded-xl bg-slate-900 hover:bg-rose-500 text-white text-xs font-bold transition-all shadow-md flex items-center justify-center gap-2">
                <span>Submit Inquiry to Provaliant Group</span>
                <i data-lucide="send" class="w-4 h-4"></i>
              </button>
            </form>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-white border-t border-slate-200 py-12 text-slate-500 text-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-wrap items-center justify-between gap-6">
      
      <div class="flex items-center gap-3">
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
      </div>

      <div>
        <p>© 2026 Provaliant Group & Provaliant Studios. All rights reserved.</p>
      </div>

    </div>
  </footer>

  <!-- Modal: IP Deep-Dive -->
  <div id="ipDetailModal" class="fixed inset-0 z-50 modal-backdrop hidden items-center justify-center p-4 md:p-6 overflow-y-auto">
    <div class="relative w-full max-w-5xl bg-white rounded-3xl shadow-2xl max-h-[92vh] overflow-y-auto border border-slate-100 animate-in fade-in zoom-in duration-200">
      <div id="ipDetailContent">
        <!-- JavaScript populates deep dive content -->
      </div>
    </div>
  </div>

  <!-- Modal: 35-Slide Deck Fullscreen Viewer -->
  <div id="deckViewerModal" class="fixed inset-0 z-50 modal-backdrop hidden items-center justify-center p-2 sm:p-6">
    <div class="relative w-full max-w-6xl bg-slate-900 text-white rounded-3xl shadow-2xl overflow-hidden border border-slate-800 flex flex-col max-h-[96vh]">
      
      <!-- Modal Top Header -->
      <div class="p-4 px-6 bg-slate-950/80 border-b border-slate-800 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <span id="deckSlideCategory" class="px-2.5 py-1 rounded-full text-[10px] font-bold bg-rose-500 text-white">
            Category
          </span>
          <h3 id="deckSlideTitle" class="text-sm sm:text-base font-bold truncate max-w-md sm:max-w-xl">
            Slide Title
          </h3>
        </div>
        <div class="flex items-center gap-3">
          <span id="deckSlideNumber" class="text-xs text-slate-400 font-medium">Slide 1 of 35</span>
          <button onclick="hIPlayApp.closeDeckModal()" class="p-2 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors">
            <i data-lucide="x" class="w-4 h-4"></i>
          </button>
        </div>
      </div>

      <!-- Main Slide Image Display -->
      <div class="flex-1 bg-slate-950 p-2 sm:p-6 flex items-center justify-center overflow-hidden relative">
        <img id="deckMainImage" src="img/Untitled copy_page-0001.jpg" alt="Slide Presentation" class="max-h-[68vh] w-auto max-w-full object-contain rounded-xl shadow-2xl" />
        
        <!-- Next / Prev Controls -->
        <button id="deckPrevBtn" onclick="hIPlayApp.prevSlide()" class="absolute left-4 top-1/2 -translate-y-1/2 p-3 rounded-full bg-slate-900/80 hover:bg-rose-500 text-white transition-colors backdrop-blur-md shadow-lg">
          <i data-lucide="chevron-left" class="w-6 h-6"></i>
        </button>
        <button id="deckNextBtn" onclick="hIPlayApp.nextSlide()" class="absolute right-4 top-1/2 -translate-y-1/2 p-3 rounded-full bg-slate-900/80 hover:bg-rose-500 text-white transition-colors backdrop-blur-md shadow-lg">
          <i data-lucide="chevron-right" class="w-6 h-6"></i>
        </button>
      </div>

      <!-- Modal Bottom Navigation Controls -->
      <div class="p-3 px-6 bg-slate-950/90 border-t border-slate-800 flex items-center justify-between text-xs">
        <span class="text-slate-400 hidden sm:inline">Use keyboard arrow keys &larr; &rarr; or buttons to navigate</span>
        <div class="flex items-center gap-2 mx-auto sm:mx-0">
          <button onclick="hIPlayApp.prevSlide()" class="py-1.5 px-4 rounded-lg bg-slate-800 hover:bg-slate-700 text-white font-bold transition-colors">
            Previous
          </button>
          <button onclick="hIPlayApp.nextSlide()" class="py-1.5 px-4 rounded-lg bg-rose-500 hover:bg-rose-600 text-white font-bold transition-colors">
            Next Slide
          </button>
        </div>
      </div>

    </div>
  </div>

  <!-- Scripts -->
  <script src="app.js"></script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html_content)
print('index.html successfully built!')
