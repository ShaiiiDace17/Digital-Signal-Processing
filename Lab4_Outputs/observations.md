# Laboratory Experiment 4 — Observations

### p32 Unit Step Function

The step is zero before 0 s and one from 0 s onward. The sampled range is 0 to 1. The transition occurs at t=0 s.

### p33 2.1 Sinusoidal Signal

All four curves have unit amplitude and one cycle over one second. The cosine curves shifted by plus or minus pi/2 align with the sine curve or its negative. Their common period is 1 s.

### p33 2.2(i) Piecewise h(t)

The signal equals 1 on -1<=t<=0 and -1 on 0<t<=2. It changes level at t=0 and is zero outside the defined intervals. The plotted interval follows the manual definition.

### p33 2.2(ii) Piecewise Exponential

The branches meet at x(0)=1. The signal is symmetric about t=0 and decreases toward both endpoints. Its endpoint values are approximately 0.3679.

### p33 2.2(iii) Piecewise f(x)

For x<0 the sine branch ranges from -1.0000 to 1.0000 on the plotted interval. The quadratic branch rises from 0 to 1 on [0,1]. For x>1 the reciprocal branch decreases toward zero.

### p34 2.2(iv) Rectangular Pulse

The visible sketch shows a pulse beginning at 2 s and ending at 4 s. This plot transcribes its apparent unit height; the manual does not show a readable analytic expression. See notes.md for the source limitation.

### p34 2.3 Exponentially Varying Sinusoid

The oscillation is bounded by envelopes that decay from +/-4 at t=0 to +/-0.001342 at t=4 s. Its angular frequency remains 6 rad/s while the amplitude decays. The phase offset of 60 degrees is converted to pi/3 radians.

### p34 2.4 Multiplication of Two Signals

At t=0 both branches of Y(t) equal 2. The negative-time exponential approaches 2, and the positive-time branch decreases linearly to -8 at 10 s. Multiplication by cos(30t) produces rapid oscillations bounded by |Y(t)|.

### p35 3.1.1 Time Shift

The shifted unit step is zero until t=2 s and one afterward. Its transition is delayed by 2 s relative to u(t). The amplitude and shape are unchanged.

### p35 3.1.2 Time Shift

The original cosine is supported on [-0.5,0.5] and peaks at t=0. The delayed curve has the same shape and peaks at t=0.5. The shift moves its features 0.5 s to the right without changing amplitude.

### p35 3.1.3 Time Shift

The diagram's triangle rises from (0,0) to (2,2), then falls to (3,0). The shifted curve retains its peak height and moves the peak to t=4. Its support moves from [0,3] to [2,5].

### p36 3.2 Time Scaling

The original cosine is supported on [-0.5,0.5]. The x(2t) version is compressed to [-0.25,0.25], while x(t/2) expands to [-1,1]. All preserve the peak amplitude of 1 at t=0.

### p37 3.3 Time Inversion

The original exponential rises from 0.0821 at -5 s to 0.6065 at -1 s. Time inversion reflects it onto [1,5], where it is exp(-t/2). The reflected curve has the same values in reverse time order.

### p38 Exercise (a) Piecewise Signal

The signal is zero for t<-4, equals t+2 on [-4,3], and equals t-2 for t>3. At -4 it takes the middle-branch value -2, and at 3 it takes value 5. The right branch starts just after 3 near 1, so there is a jump there.

### p38 Exercise (b)(i) x(t-1)

The transformation x(t-1) delays the signal by 1 time unit. Its breakpoints move from -4 and 3 to -3 and 4. The branch values are those of x evaluated one unit earlier.

### p38 Exercise (b)(ii) x(t/3)

The transformation x(t/3) expands the time axis by a factor of 3. Its breakpoints move to -12 and 9. The branch values are evaluated at one-third of the plotted time.

### p38 Exercise (b)(iii) x(-t)

Time inversion reflects the piecewise signal across t=0. The original breakpoints -4 and 3 appear at 4 and -3. The values are obtained by evaluating x at the negative of the plotted time.
