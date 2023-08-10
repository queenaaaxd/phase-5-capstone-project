import React from "react";
import ProductCard from './ProductCard';

function ProductList({ products, addToCart }) {
    
    // map
    const productsDisplay = products.map((product) => <ProductCard product={product} key={product.id} addToCart={addToCart} />)

    return (

        <ul className="cards">{productsDisplay}</ul>

    );
}

export default ProductList;
