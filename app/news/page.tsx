const newsItems = [
  { date: "2026.09.19", title: "公式サイトを公開しました" },
  { date: "2026.09.16", title: "Project YURA 開発進捗" },
  { date: "2026.09.13", title: "MEMORIELA プロジェクト始動" },
];

export default function NewsPage() {
  return (
    <main className="subpage">
      <header className="subpageHeader">
        <a className="wordmark" href="/">MEMORIELA - Project.YURA</a>
        <nav aria-label="Main navigation">
          <a href="/about">About</a>
          <a href="/technology">Technology</a>
          <a href="/gallery">Gallery</a>
          <a className="active" href="/news">News</a>
          <a href="/contact">Contact</a>
        </nav>
      </header>

      <section className="subpageHero center">
        <span>LATEST NEWS</span>
        <h1>News</h1>
        <p>最新情報</p>
      </section>

      <section className="subpageContent">
        <div className="timeline">
          {newsItems.map((item) => (
            <article key={item.date + item.title}>
              <time>{item.date}</time>
              <i />
              <div><h3>{item.title}</h3></div>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}
