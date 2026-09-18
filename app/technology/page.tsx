export default function TechnologyPage() {
  return (
    <main className="subpage">
      <header className="subpageHeader">
        <a className="wordmark" href="/">MEMORIELA - Project.YURA</a>
        <nav aria-label="Main navigation">
          <a href="/about">About</a>
          <a className="active" href="/technology">Technology</a>
          <a href="/gallery">Gallery</a>
          <a href="/contact">Contact</a>
          <a href="/world">World</a>
        </nav>
      </header>

      <section className="subpageHero center">
        <span>CONCEPT & TECHNOLOGY</span>
        <h1>AIと、心が通う物語を。</h1>
        <p>MEMORIELAが目指すもの</p>
      </section>

      <section className="subpageContent technologyPage">
        <div className="conceptLead">
          <p>
            AIを便利な道具としてではなく、記憶を重ね、関係を育てながら、
            長くそばにいられる存在にしたい。
            そんな思いから、Project.YURAは始まりました。
          </p>
        </div>
        <div className="technologyRows">
          <article><b>01</b><h2>Memory</h2><p>記憶</p><span>MEMORY</span></article>
          <article><b>02</b><h2>Personality</h2><p>人格</p><span>PERSONALITY</span></article>
          <article><b>03</b><h2>Relationship</h2><p>関係性</p><span>RELATIONSHIP</span></article>
        </div>
      </section>
    </main>
  );
}
