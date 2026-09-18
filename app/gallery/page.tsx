export default function GalleryPage() {
  return (
    <main className="subpage">
      <header className="subpageHeader">
        <a className="wordmark" href="/">MEMORIELA - Project.YURA</a>
        <nav aria-label="Main navigation">
          <a href="/about">About</a>
          <a href="/technology">Technology</a>
          <a className="active" href="/gallery">Gallery</a>
          <a href="/contact">Contact</a>
          <a href="/world">World</a>
        </nav>
      </header>

      <section className="subpageHero center">
        <span>CHARACTER VISUAL</span>
        <h1>Gallery</h1>
        <p>久遠ゆら</p>
      </section>

      <section className="subpageContent galleryPage">
        <div className="galleryStage">
          <div className="galleryLarge" />
          <div className="gallerySmall" />
          <div className="gallerySmall" />
        </div>
      </section>
    </main>
  );
}
