import React from "react";
import AliceCarousel from "react-alice-carousel";
import "react-alice-carousel/lib/alice-carousel.css";

function Home() {

const responsive = {
    0: {
        items: 1,
    },
    568: {
        items: 2,
    },
    1024: {
        items: 3,
        itemsFit: "contain",
    },
};
    
    const items = [
    <div className="item">
        <img src="/essentia_water.png" alt="essentia" />
    </div>,
    <div className="item">
        <img src="/celsius_orange.png" alt="celsius" />
    </div>,
    <div className="item">
        <img src="/harmless_water.png" alt="harmless" />
        </div>,
    <div className="item">
        <img src="/harmless_water.png" alt="harmless" />
    </div>,
    <div className="item" data-value="2">
    </div>,
    ];

    return (
        <div>
            <AliceCarousel mouseTracking items={items} responsive={responsive} />
        </div>
    );
}

export default Home;