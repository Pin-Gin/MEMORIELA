const xUrl = "https://x.com/MEMORIELA_JP";
const youtubeUrl = "https://youtube.com/@MEMORIELA";

const topics = [
  { date: "2026.09.19", title: "公式サイトを公開しました", isNew: true },
  { date: "2026.09.16", title: "Project YURA 開発進捗" },
  { date: "2026.09.13", title: "MEMORIELA プロジェクト始動" },
];

const mobileNavItems = [
  { href: "/characters", icon: "◇", label: "Characters", sub: "キャラクター" },
  { href: "/technology", icon: "✦", label: "Technology", sub: "テクノロジー" },
  { href: "/gallery", icon: "▣", label: "Gallery", sub: "ビジュアル" },
  { href: "/news", icon: "◎", label: "News", sub: "最新情報" },
];

export default function Home() {
  return (
    <main>
      <section className="hero desktopHero" id="home">
        <header className="heroHeader">
          <a className="wordmark" href="/">MEMORIELA - Project.YURA</a>
          <nav aria-label="Main navigation">
            <a href="/characters">Characters</a>
            <a href="/technology">Technology</a>
            <a href="/gallery">Gallery</a>
            <a href="/world">World</a>
          </nav>
          <div className="heroActions"><a href="/contact">Contact</a><b>☰</b></div>
        </header>

        <aside className="heroTopics" aria-label="Latest topics">
          <div className="heroTopicsHead">
            <b>LATEST TOPICS</b>
            <a href="/news">一覧を見る →</a>
          </div>

          <div className="heroTopicsList">
            {topics.map((item) => (
              <article key={item.date + item.title}>
                <time>{item.date}</time>
                <p>{item.title}</p>
                {item.isNew && <strong>NEW</strong>}
              </article>
            ))}
          </div>

          <a className="historyLink" href="/history" aria-label="Development History">
            <div>
              <b>Development History</b>
              <span>これまでの開発記録を見る</span>
            </div>
            <i aria-hidden="true" />
          </a>
        </aside>

        <div className="heroBottom">
          <span># Project.YURA　｜　# 開発局　｜　# AI × Creativity</span>
          <b>SCROLL</b>
        </div>
      </section>

      <section className="mobileHome" aria-label="MEMORIELA mobile home">
        <section className="mobileHero">
          <header className="mobileHeroHeader">
            <a className="mobileWordmark" href="/">
              <strong>MEMORIELA</strong>
              <span>Project.YURA</span>
            </a>
            <div className="mobileHeroActions">
              <a href="/contact">Contact</a>
              <b aria-hidden="true">☰</b>
            </div>
          </header>

          <div className="mobileHeroVisual" aria-hidden="true">
            <i className="mobileHeroFrame" />
          </div>

          <div className="mobileHeroCopy">
            <span>MEMORIELA</span>
            <h1>Project.YURA</h1>
            <p>Memories live with you.</p>
          </div>

          <div className="mobileHeroSignature" aria-hidden="true">
            <em>Yura</em>
            <span>KUON YURA</span>
          </div>
        </section>

        <nav className="mobilePrimaryNav" aria-label="Mobile primary navigation">
          {mobileNavItems.map((item) => (
            <a href={item.href} key={item.href}>
              <i aria-hidden="true">{item.icon}</i>
              <strong>{item.label}</strong>
              <span>{item.sub}</span>
            </a>
          ))}
        </nav>

        <a className="mobileWorldBand" href="/world">
          <div className="mobileWorldVisual" aria-hidden="true">
            <span>MEMORIELA</span>
          </div>
          <div className="mobileWorldCopy">
            <span>MEMORIELA WORLD</span>
            <p>漫画・物語・日常</p>
            <b>詳しく見る　→</b>
          </div>
        </a>
      </section>

      <footer>
        <div><strong>MEMORIELA</strong><span>Project.YURA</span></div>
        <nav>
          <a href="/characters">Characters</a>
          <a href="/technology">Technology</a>
          <a href="/gallery">Gallery</a>
          <a href="/contact">Contact</a>
          <a href="/world">World</a>
        </nav>
        <div className="social"><a href={xUrl} target="_blank" rel="noreferrer">Official X</a><a href={youtubeUrl} target="_blank" rel="noreferrer">YouTube</a></div>
        <small>© 2026 MEMORIELA. All rights reserved.</small>
      </footer>
    </main>
  );
}
