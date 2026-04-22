<div class="map">
  <iframe src="https://affectabot.forge.apps.education.fr/"></iframe>
</div>

<style>
/* Neutraliser les contraintes de Material sur toute la chaîne parente */
.md-main,
.md-main__inner,
.md-content,
.md-content__inner {
  height: 100% !important;
  max-width: 100% !important;
  padding: 0 !important;
  margin: 0 !important;
  flex: 1 1 auto !important;
  display: flex !important;
  flex-direction: column !important;
}

.map {
  flex: 1 1 auto !important;
  display: flex !important;
  width: 100% !important;
  height: calc(100vh - 48px) !important; /* 48px = hauteur du header Material */
  min-height: 0 !important; /* Crucial pour flex children */
}

iframe {
  flex: 1 1 auto !important;
  width: 100% !important;
  height: 100% !important;
  border: none !important;
  display: block !important;
}

.md-main,
.md-main__inner,
.md-content,
.md-content__inner,
.md-content__inner > :first-child {
  margin: 0 !important;
  padding: 0 !important;
}

.md-content__inner::before,
.md-content__inner::after {
  display: none !important;
}
</style>