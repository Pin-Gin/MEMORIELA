export default function WorldPage() {
  return (
    <main className="subpage">
      <header className="subpageHeader">
        <a className="wordmark" href="/">MEMORIELA - Project.YURA</a>
        <nav aria-label="Main navigation">
          <a href="/about">About</a>
          <a href="/technology">Technology</a>
          <a href="/gallery">Gallery</a>
          <a href="/contact">Contact</a>
        </nav>
      </header>

      <section className="subpageHero center">
        <span>MEMORIELA WORLD</span>
        <h1>World</h1>
        <p>漫画・物語・日常</p>
      </section>

      <section className="simplePage">
        <p>Project.YURAの世界を、漫画や物語、日常の断片を通して届けます。</p>
      </section>
    </main>
  );
}
