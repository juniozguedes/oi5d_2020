import React, {useState, useEffect} from 'react';
import './App.css';

import {loadStripe} from '@stripe/stripe-js';

function App() {

  const [example, setExample] = useState()
  useEffect(()=>{
    fetch('http://localhost:8000/checkout/').then(response=>response.json().then(asbaba=>setExample(asbaba)))
  },[])

  async function getStripe(){
    const stripe = await loadStripe('pk_test_yHqlD7RhmVmxX9zUSK3PMxlL00cvbk93VA');
    stripe.redirectToCheckout({
      sessionId: example.session_id
    })
    }
  return (
    <div className="App">
      <button onClick={getStripe} id="checkout-button">Checkout</button>
    </div>
  );
}

export default App;