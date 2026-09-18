const xUrl = "https://x.com/MEMORIELA_JP";

const topics = [
  { date: "2026.09.16", title: "久遠ゆら 公式ビジュアル公開", isNew: true },
  { date: "2026.09.11", title: "久遠ゆら 公式ビジュアル正式決定" },
  { date: "2026.09.06", title: "チャットUI実装" },
  { date: "2026.09.03", title: "サイトデザイン リニューアル" },
  { date: "2026.08.28", title: "Project.YURA 進捗報告" },
];

export default function Home() {
  return (
    <main>
      <section className="hero" id="home">
        <header className="heroHeader">
          <a className="wordmark" href="/">MEMORIELA - Project.YURA.</a>
          <nav aria-label="Main navigation">
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/technology">Technology</a>
            <a href="/gallery">Gallery</a>
            <a href="/history">Development History</a>
          </nav>
          <div className="heroActions"><span>開発局</span><b>☰</b></div>
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
            <i>→</i>
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
          <a href="/">Home</a>
          <a href="/about">About</a>
          <a href="/technology">Technology</a>
          <a href="/gallery">Gallery</a>
          <a href="/history">Development History</a>
        </nav>
        <div className="social"><a href={xUrl} target="_blank" rel="noreferrer">Official X</a><span>YouTube</span></div>
        <small>© 2026 MEMORIELA. All rights reserved.</small>
      </footer>
    </main>
  );
}
