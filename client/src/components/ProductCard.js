import React, { useState } from "react";

function ProductList({ product, addToCart }) {
  const [quantity, setQuantity] = useState(1);

  const handleQuantityChange = (e) => {
    setQuantity(parseInt(e.target.value));
  };

  console.log(product.image);

  return (
    <li className="card">
      <img src={product.image} alt={product.name} />
      <h4>{product.name}</h4>
      <p>${product.price}</p>
      <select value={quantity} onChange={handleQuantityChange}>
        <option key={1} value={1}>
          1
        </option>
        <option key={2} value={2}>
          2
        </option>
        <option key={3} value={3}>
          3
        </option>
        <option key={4} value={4}>
          4
        </option>
        <option key={5} value={5}>
          5
        </option>
      </select>
      <button onClick={addToCart(product)}>ADD TO CART</button>
    </li>
  );
}

export default ProductList;
