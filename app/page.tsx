const xUrl = "https://x.com/MEMORIELA_JP";

const topics = [
  { date: "2026.09.19", title: "公式サイトを公開しました", isNew: true },
  { date: "2026.09.16", title: "Project YURA 開発進捗" },
  { date: "2026.09.13", title: "MEMORIELA プロジェクト始動" },
];

export default function Home() {
  return (
    <main>
      <section className="hero" id="home">
        <header className="heroHeader">
          <a className="wordmark" href="/">MEMORIELA - Project.YURA</a>
          <nav aria-label="Main navigation">
            <a href="/about">About</a>
            <a href="/technology">Technology</a>
            <a href="/gallery">Gallery</a>
            <a href="/world">World</a>
          </nav>
          <div className="heroActions"><a href="/contact">Contact</a><b>☰</b></div>
        </header>

        <aside className="heroTopics" aria-label="Latest topics">
          <div className="heroTopicsHead">
            <b>LATEST TOPICS</b>
            <span>一覧を見る →</span>
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

      <footer>
        <div><strong>MEMORIELA</strong><span>Project.YURA</span></div>
        <nav>
          <a href="/about">About</a>
          <a href="/technology">Technology</a>
          <a href="/gallery">Gallery</a>
          <a href="/world">World</a>
          <a href="/contact">Contact</a>
        </nav>
        <div className="social"><a href={xUrl} target="_blank" rel="noreferrer">Official X</a><span>YouTube</span></div>
        <small>© 2026 MEMORIELA. All rights reserved.</small>
      </footer>
    </main>
  );
}
