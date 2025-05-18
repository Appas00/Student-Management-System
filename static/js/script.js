document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".card");

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show");
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    cards.forEach(card => {
        card.classList.add("hidden");
        observer.observe(card);
    });
});
// 3D hover tilt for cards
document.addEventListener("mousemove", (e) => {
    document.querySelectorAll(".card-3d").forEach(card => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = ((y - centerY) / centerY) * 10;
        const rotateY = ((x - centerX) / centerX) * -10;

        card.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });
});

document.addEventListener("mouseleave", () => {
    document.querySelectorAll(".card-3d").forEach(card => {
        card.style.transform = "rotateX(0deg) rotateY(0deg)";
    });
});
