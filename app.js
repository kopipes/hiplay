/**
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
    theme: 'The Panji Universe is a world where stories are not merely fairy tales, but the source of life\'s energy. As long as humans continue to tell stories, the Realm of Legends remains alive. At the center stands the Dewandaru Tree, the source of all Nusantara legends. When cut down by Jagad Peteng, the world of stories began to crumble, and a new generation of Panji must be found to bring it back to life.',
    background: 'PROVALIANT STUDIO\'s flagship original IP, Legenda Panji Universe, reimagines East Javanese folklore into a global franchise. With strong expertise in licensed merchandise, IP collaborations, and brand activations, Provaliant is committed to revitalizing local stories as a symbol of the rising creative spirit of the Nusantara.',
    characters: ['Panji (Nusantara Hero)', 'Krucil Tigris (White Tiger)', 'Krucil Garuda/Owl (Sage Guardian)', 'Dewandaru Spirits'],
    metrics: [
      { label: 'Heritage', val: 'UNESCO Recognized' },
      { label: 'Scope', val: 'Global Multiverse' },
      { label: 'Formats', val: 'Film, Animation & Merch' }
    ],
    coverImage: 'img/slide-06.jpg',
    styleGuideImage: 'img/slide-08.jpg',
    merchImage: 'img/slide-07.jpg',
    mascotImage: 'img/slide-09.jpg',
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
    theme: 'As Companions, Milk Mocha Bear can be partners, couple, friends, or pals. They complete each other\'s traits and personalities. They can represent you and your companion through themes of love, emotion, food sharing, and cozy moments.',
    background: 'Launched as LINE sticker characters in 2016, Milk Mocha Bear quickly gained immense global popularity through cute animations and became the first Indonesian creator stickers featured in the Official LINE Sticker MVP Program. Today, Milk Mocha Bear is a global brand with over 1 million followers led by audiences in India, USA, and Indonesia, with a consistent 14% Instagram engagement rate (155.5K likes and 2.5K comments per post).',
    characters: ['Milk (Cheerful White Bear)', 'Mocha (Caring Brown Bear)', 'Matcha (Little Dino Companion)'],
    metrics: [
      { label: 'Global Followers', val: '1,000,000+' },
      { label: 'IG Engagement', val: '14.0% (Avg 1-3%)' },
      { label: 'Avg Likes / Post', val: '155.5K+' }
    ],
    coverImage: 'img/slide-14.jpg',
    styleGuideImage: 'img/slide-15.jpg',
    merchImage: 'img/slide-16.jpg',
    slides: [14, 15, 16],
    merchHighlights: ['Eco-friendly tote bags & commuter canvas bags', 'Double-wall stainless tumblers & pastel flasks', 'Embroidered dad caps & soft pastel tees', 'Couple plushies, keychains & pouch sets']
  },
  {
    id: 'si-juki',
    name: 'Si Juki',
    studio: 'Created by Faza Meonk / PIONICON',
    type: 'collab',
    categoryTag: 'Pop Culture • Youth & Satire',
    badge: '👑 Indonesia\'s #1 Comic IP',
    accentColor: '#EAB308',
    tagline: 'The Legendary Maverick of Indonesian Pop Culture & Everyday Satire',
    summary: 'Indonesia\'s most iconic and commercially successful comic character, famous for witty humor, streetwise charm, blockbuster animated movies, and lifestyle streetwear.',
    theme: 'Si Juki is one of Indonesia\'s most iconic comic characters, known for his witty humor, rebellious charm, and unpredictable way of solving everyday problems from student struggles to modern work hustle.',
    background: 'Born from a sketch in 2010, Si Juki debuted in the bestselling comic \'Ngampus!!! Buka-bukaan Aib Mahasiswa\'. Since then, the character has grown into one of Indonesia\'s leading pop culture IPs, expanding into animated films, TV series, merchandise, apparel, games, and collaborations with brands, media, and government institutions.',
    characters: ['Si Juki', 'Prof. Juned', 'Mang Awung', 'Coro the Cockroach'],
    metrics: [
      { label: 'Debut Year', val: '2010' },
      { label: 'Media Reach', val: 'Theatrical Movies & TV' },
      { label: 'Audience', val: 'Gen Z, Millennials & Youth' }
    ],
    coverImage: 'img/slide-17.jpg',
    styleGuideImage: 'img/slide-18.jpg',
    merchImage: 'img/slide-19.jpg',
    mascotImage: 'img/slide-04.jpg',
    slides: [17, 18, 19, 4],
    merchHighlights: ['Hustle & \'Kerja Keras / Scroll Lebih Keras\' graphic apparel', 'Canvas messenger & \'Out of the Box\' tote bags', 'FOMO & \'Ngutang Dulu\' acrylic keychains', '\'Overthinking\' streetwear dad caps & tumblers']
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
    coverImage: 'img/slide-20.jpg',
    styleGuideImage: 'img/slide-21.jpg',
    merchImage: 'img/slide-22.jpg',
    mascotImage: 'img/slide-04.jpg',
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
    tagline: 'Empowering Children\'s Imagination with 1,000+ Character World',
    summary: 'A multi-award winning early childhood ecosystem featuring animated series, TikTok micro-content, 55 published storybook titles, and original sing-along songs.',
    theme: 'Fun Cican is part of M.C. Bunny (Mushroom Cut Bunny), spreading kindness, creativity, positive habits, and musical adventures to children and young families.',
    background: 'A local Indonesian IP built through an ecosystem of micro-content, including TikTok, animated series, 55 storybook titles, and dozens of original songs. With a roadmap of up to 1,025 characters, the IP is designed to grow into comics, OTT content, games, and other storytelling formats.',
    characters: ['Cican (Mushroom Cut Bunny)', 'Cici', 'Kebon Friends', 'Alien Pals'],
    metrics: [
      { label: 'Storybooks', val: '55 Published Titles' },
      { label: 'Character Roadmap', val: 'Up to 1,025 Characters' },
      { label: 'Formats', val: 'Books, Songs, OTT & Series' }
    ],
    coverImage: 'img/slide-23.jpg',
    styleGuideImage: 'img/slide-24.jpg',
    merchImage: 'img/slide-25.jpg',
    mascotImage: 'img/slide-04.jpg',
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
    theme: 'Kidbash is a story about redefining heroism. It speaks for forgotten characters and those who were never meant to shine. True heroes aren\'t defined by spectacle, but by sacrifice, by what they are willing to give to those in need. Kidbash awakens with no memory of his past, knowing only his name and dream of becoming a hero. After failing to protect Mandala Village, he begins a journey to find the legendary master Tao Shen Long.',
    background: 'Combining 3D video-game aesthetics, retro pixel art nostalgia, and modern superhero storytelling into a high-energy IP universe.',
    characters: ['Kidbash (Heroic Kid)', 'Master Tao Shen Long', 'Mandala Guardians'],
    metrics: [
      { label: 'Visual Style', val: '3D Arcade & Pixel Nostalgia' },
      { label: 'Core Theme', val: 'Empathy, Persistence & Courage' },
      { label: 'Audience', val: 'Gamers, Anime Fans & Youth' }
    ],
    coverImage: 'img/slide-26.jpg',
    styleGuideImage: 'img/slide-27.jpg',
    merchImage: 'img/slide-28.jpg',
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
    coverImage: 'img/slide-29.jpg',
    styleGuideImage: 'img/slide-30.jpg',
    merchImage: 'img/slide-31.jpg',
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
    coverImage: 'img/slide-10.jpg',
    merchImage: 'img/slide-11.jpg',
    mascotImage: 'img/slide-04.jpg',
    slides: [10, 11, 4, 34],
    merchHighlights: ['Jungle explorer roll-top backpacks', 'Dino Island Team jerseys & graphic shirts', 'Custom sculpted prehistoric dinosaur mugs', 'Explorer badge caps, lanyards & pins']
  }
];

const ALL_SLIDES = Array.from({ length: 35 }, (_, i) => {
  const num = i + 1;
  const pad = String(num).padStart(2, '0');
  let title = 'hIPlay Presentation Deck - Slide ' + num;
  let category = 'Overview';
  
  if (num === 1) { title = 'Introducing hIPlay - Indonesia\'s IP Playground'; category = 'Intro'; }
  else if (num === 2) { title = 'Our Mission: Boosting Indonesia\'s Creative Economy'; category = 'Mission'; }
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

    const mailto = 'mailto:nungky@provaliantgroup.com,chandra@provaliantgroup.com?subject=hIPlay Partnership Inquiry from ' + encodeURIComponent(company) + ' - ' + encodeURIComponent(name) + '&body=' + encodeURIComponent('Name: ' + name + '\nCompany: ' + company + '\nEmail: ' + email + '\nPhone: ' + phone + '\nIP of Interest: ' + ipInterest + '\n\nMessage:\n' + message);
    
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
