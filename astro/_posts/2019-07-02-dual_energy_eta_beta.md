---
layout: post
title:  "Cholla_PM: Dual Energy Eta Beta and Pressure Jump"
date:   2019-07-02 17:10:24 -0800
categories: cholla
---

The simulations are $$128^3$$ and 50Mpc.

**Dual Energy Parameters:** $$\eta=0.005$$   $$\beta_0 = 0.25$$   $$\beta_1 = 0.0$$

**Pressure Jump:**

From Fryxell 200 the Pressure Jump Condition for shock detection is:

 $$\frac{\left|\langle P\rangle_{i+1}^{n}-\langle P\rangle_{i-1}^{n}\right|}{\min \left(\langle P\rangle_{i+1}^{n},\langle P\rangle_{i-1}^{n}\right)}> \alpha \gamma \frac{\left|\langle\rho\rangle_{i+1}^{n}-\langle\rho\rangle_{i-1}^{n}\right|}{\min \left(\langle\rho\rangle_{i+1}^{n},\langle\rho\rangle_{i-1}^{n}\right)}$$
 
 Their implementation uses $$\alpha = 0.1$$.
 
 