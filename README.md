# Introduction to Numerical Analysis
Course _Introduction to Numerical Analysis_ at NTU.<br />
All codes are using Python36.<br />

## Lecture
  - **Lecture201** -Approximation errors and Roundoff errors<br />
  practice1 : Calculating pi with Liu Hui method.<br />
  practice2 : Calculating pi with Riemann zeta function.<br />
  - **Lecture202** -Numerical differential and integration<br />
  practice1 : Integral with Simpson 3/8 method.<br />
  practice2 : Difference between different interval using `scipy.integrate`.<br />
  - **Lecture203** -Numpy array and matplotlib.<br />
  practice1 : Some basic array operation.<br />
  practice2 : Using `matplotlib.pyplot` to plot functions.<br />
  - **Lecture204** -Linear algebra and matplotlib image processing.<br />
  practice1 : Use `np.linalg.inv` and `np.linalg.det` to verfiy some properties.<br />
  practice2 : Use `plt.imread` to read and process image, `plt.imshow` and `plt.show` to show image.<br />
  - **Lecture205** -Root finding, curve fitting, and minimization.<br />
  practice1 : Use `scipy.optimize.newton` to find root by Newton's method, and build arcsin, arccos functions.<br />
  practice2 : Use `np.polyfit` to fit, `plt.errorbar` to plot data with error.<br />
  
## Assignment
  - **Assignment1**<br />
  1-1 : Simply numerical differential using `scipy.misc`.<br/>
  1-2 : Simply numerical integration using `scipy.integrate`.<br />
  1-3 : Convolution, Breit-Wigner distribution, Gaussian distribution using `scipy.integrate`.<br />
  - **Assignment2**<br />
  2-1 : Array operation using `np.fromfunction`.<br />
  2-2 : Array operation using `np.fromfunction`.<br />
  2-3 : Use `np.array` to play _Game of Life_.<br />
  - **Assignment3**<br />
  3-1 : Use `scipy.linalg.solve` to solve equation.<br />
  3-2 : Use `np.diag`,`np.sqrt` to compute covariance matrix into correlation matrix.<br />
  3-3 : Computing least square. Code involved `np.linspace`, `np.dot`, `np.transpose`.<br />
  - **Assignment4**<br />
  4-1 : Use `scipy.optimize.newton` to find root by Newton's method.<br />
  4-2 : Use `scipy.optimize.minimize` to fit data with error range by calculating X^2.<br />
  4-3 : Use `np.hstack`, `plt.hist` to build histograms. Then try to maximize a given function by `scipy.optimize.minimize`.<br />
  - **Assignment5**<br />
  5-1 : Use `scipy.integrate.solve_ivp` to solve position, velocity, acceleration, with resistance force ODE.<br />
  5-2 : Use `scipy.integrate.solve_ivp` to solve ODE a multi-star system in 2D.<br />
  5-3 : Use `scipy.integrate.solve_ivp` to solve ODE charged particle moving in magnetic field and electric field.<br />
  - **Assignment6**<br />
  6-1 : Use `np.random.rand` to generate random number within the target function distribution.<br />
  6-2 : Use `np.random.rand` to generate a unit circle's chord.<br />
  6-3 : Use `np.random.rand` to generate smeared exponential decay Gaussian distribution function.<br />
  
