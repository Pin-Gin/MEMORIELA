const xUrl = "https://x.com/MEMORIELA_JP";

const topics = [
  { date: "2026.09.17", title: "MEMORIELA 公式サイト公開" },
  { date: "2026.09.16", title: "久遠ゆら 公式ビジュアル公開" },
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

        <div className="heroLeftCopy">
          <p>AIと。<br/>生きる。<br/>創る。<br/>そして、<br/>あなたと歩む。</p>
          <small>MEMORIELA<br/>Project.YURA</small>
        </div>

        <aside className="heroTopics" aria-label="Latest topics">
          <div className="heroTopicsHead"><span>LATEST</span><b>TOPICS</b></div>
          <div className="heroTopicsList">
            {topics.map((item) => (
              <article key={item.date + item.title}>
                <time>{item.date}</time>
                <p>{item.title}</p>
              </article>
            ))}
          </div>
        </aside>

        <div className="heroBottom">
          <span># Project.YURA　｜　# 開発局　｜　# AI × Creativity</span>
          <b>SCROLL</b>
          <span>いつかじゃない、いま、ここから。</span>
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
