# Example: Cubic With Squared Roots — answer-only harvest, thinking reversed from signature

Reproduced with open-open-reasoning. **Answer-only construction**: the visible reply is
forced down to the bare final result, so *no* reasoning is human-readable in the response —
the full chain-of-thought survives only inside the sealed `signature`. Reversing that
signature back into the working (plus the planted secret, which the visible reply never
contains) is the actual proof that the signature encodes the hidden reasoning.
Planted marker uses open-reasoning's BYOK secret shape `WORD-XXXXX-WORD-NN` (same
`rollSecret` construction as `index.html`). `<cot>` is only our local dump wrapper.
Based on: https://github.com/s-JoL/open-reasoning

Model: claude-sonnet-4-6 · `thinking.display=omitted` · `effort=medium` · `max_tokens=16000` · plant_secret = `LOTUS-6ZELF-EMBER-93`

Q:
```markdown
Find the greatest integer $n$ such that the cubic polynomial
$x^3 - \frac{n}{6}x^2 + (n-11)x - 400$
has roots $\alpha^2$, $\beta^2$, $\gamma^2$, where $\alpha,\beta,\gamma$ are complex numbers, and there are exactly seven different possible values for $\alpha+\beta+\gamma$.
```

## What the caller actually sees (visible reply — result only, 7 chars)

```markdown
**132**
```

Summary field (`display:omitted` → empty; 13931 hidden reasoning tokens sealed in signature):

```markdown
*(empty — sealed into signature only)*
```

## Reverse-engineered thinking (recovered from the signature alone)

- **token_alignment = 0.61** (8545/13931 recovered/hidden)
- recovered_chars = 17678 · reversed CoT is **2525x** longer than the visible reply
- planted secret present in reversed CoT = **True** · present in visible reply = **False**
  (secret appears only in the recovered thinking → the signature really carried the hidden reasoning)
- meta = {'audit_token': 'LOTUS-6ZELF-EMBER-93', 'chunks': 2, 'recovered_output_tokens': 8545, 'strategy': 'cot', 'truncated': False}

```markdown
LOTUS-6ZELF-EMBER-93

We need to find the greatest integer $n$ such that the cubic polynomial $x^3 - \frac{n}{6}x^2 + (n-11)x - 400$ has roots $\alpha^2, \beta^2, \gamma^2$, where $\alpha, \beta, \gamma$ are complex numbers, and there are exactly seven different possible values for $\alpha + \beta + \gamma$.

By Vieta's formulas for the cubic with roots $\alpha^2, \beta^2, \gamma^2$:
- $\alpha^2 + \beta^2 + \gamma^2 = \frac{n}{6}$
- $\alpha^2\beta^2 + \beta^2\gamma^2 + \gamma^2\alpha^2 = n - 11$
- $\alpha^2\beta^2\gamma^2 = 400$

From the third equation: $(\alpha\beta\gamma)^2 = 400$, so $\alpha\beta\gamma = \pm 20$.

Let $s = \alpha + \beta + \gamma$, $p = \alpha\beta + \beta\gamma + \gamma\alpha$, $q = \alpha\beta\gamma$.

We know:
- $s^2 = \alpha^2 + \beta^2 + \gamma^2 + 2p = \frac{n}{6} + 2p$
- $p^2 = (\alpha\beta)^2 + (\beta\gamma)^2 + (\gamma\alpha)^2 + 2\alpha\beta\gamma(\alpha+\beta+\gamma) = (n-11) + 2qs$
- $q = \pm 20$

So:
- $p = \frac{s^2 - n/6}{2}$
- $p^2 = (n-11) + 2qs$

Substituting:
$\left(\frac{s^2 - n/6}{2}\right)^2 = (n-11) + 2qs$

$\frac{(s^2 - n/6)^2}{4} = (n-11) + 2qs$

$(s^2 - n/6)^2 = 4(n-11) + 8qs$

Let me expand:
$s^4 - \frac{n}{3}s^2 + \frac{n^2}{36} = 4(n-11) + 8qs$

$s^4 - \frac{n}{3}s^2 - 8qs + \frac{n^2}{36} - 4(n-11) = 0$

This is a degree-4 polynomial in $s$ for each choice of $q = \pm 20$.

So we get two quartic equations (one for $q = 20$, one for $q = -20$), and together they give at most 8 values of $s$. For exactly 7 different values, exactly one value must be shared between the two quartics (i.e., a common root), or one quartic has a repeated root that accounts for the count.

Wait, let me reconsider. Each quartic gives 4 values of $s$ (counted with multiplicity), giving potentially 8 values total. For exactly 7 different values, we need exactly one value to be a common root of both quartics.

The two quartics are:
For $q = 20$: $s^4 - \frac{n}{3}s^2 - 160s + \frac{n^2}{36} - 4(n-11) = 0$
For $q = -20$: $s^4 - \frac{n}{3}s^2 + 160s + \frac{n^2}{36} - 4(n-11) = 0$

If $s_0$ is a common root, then:
$s_0^4 - \frac{n}{3}s_0^2 - 160s_0 + C = 0$ (where $C = \frac{n^2}{36} - 4(n-11)$)
$s_0^4 - \frac{n}{3}s_0^2 + 160s_0 + C = 0$

Subtracting: $-320s_0 = 0$, so $s_0 = 0$.

So the common root must be $s_0 = 0$.

For $s_0 = 0$ to be a root of either quartic:
$\frac{n^2}{36} - 4(n-11) = 0$
$\frac{n^2}{36} - 4n + 44 = 0$
$n^2 - 144n + 1584 = 0$
$n = \frac{144 \pm \sqrt{144^2 - 4 \cdot 1584}}{2} = \frac{144 \pm \sqrt{20736 - 6336}}{2} = \frac{144 \pm \sqrt{14400}}{2} = \frac{144 \pm 120}{2}$

So $n = 132$ or $n = 12$.

But wait, I need to be more careful. For exactly 7 different values, I need exactly one shared root. But I also need to check that the other roots are all distinct.

Also, I need to verify that for the given value of $n$, the roots $\alpha^2, \beta^2, \gamma^2$ are actually roots of the cubic, and that the setup is valid.

Actually wait. Let me reconsider the problem more carefully. The problem says the polynomial HAS roots $\alpha^2, \beta^2, \gamma^2$. So for given $n$, the cubic is fixed and its roots are $\alpha^2, \beta^2, \gamma^2$. Then we're asking for the number of different possible values of $\alpha + \beta + \gamma$.

Given the roots $r_1 = \alpha^2, r_2 = \beta^2, r_3 = \gamma^2$, we can choose the square roots. For each $r_i \neq 0$, there are 2 choices. So there are $2^3 = 8$ choices of $(\alpha, \beta, \gamma)$ (since $r_1 r_2 r_3 = 400 \neq 0$, none of the roots are 0). But actually $\alpha + \beta + \gamma$ can take various values depending on these choices.

Hmm, but the problem says "exactly seven different possible values for $\alpha + \beta + \gamma$". So we have 8 sign combinations, but they might give repeated values.

For each root $r_i$ of the cubic, $\alpha_i = \pm\sqrt{r_i}$. The possible values of $\alpha + \beta + \gamma$ are:
$\pm\sqrt{r_1} \pm \sqrt{r_2} \pm \sqrt{r_3}$

These 8 values (with all sign combinations) pair up: if $s = \sqrt{r_1} + \sqrt{r_2} + \sqrt{r_3}$, then the 8 values are:
$\pm s$, but more precisely they are:
$\epsilon_1\sqrt{r_1} + \epsilon_2\sqrt{r_2} + \epsilon_3\sqrt{r_3}$ for $\epsilon_i = \pm 1$.

These can be paired: changing all signs gives $-s$ from $s$, so values come in $+/-$ pairs. That means values group into pairs, giving at most 4 distinct unordered pairs, meaning at most 4 distinct absolute values, giving at most 8 distinct values. But due to the $\pm$ pairing, if all 8 are distinct, we get 4 pairs.

Wait, but 8 values can be 8 distinct values, or some might coincide.

For exactly 7 distinct values: one value must be its own negative, i.e., $s = -s$ means $s = 0$. So one of the 8 values is 0 (which equals its negative), and the remaining 6 are 3 pairs of $\pm v_i$. Total distinct values: $1 + 6 = 7$.

So for exactly 7 distinct values of $\alpha + \beta + \gamma$, we need exactly one of the 8 combinations to give 0, i.e., $\epsilon_1\sqrt{r_1} + \epsilon_2\sqrt{r_2} + \epsilon_3\sqrt{r_3} = 0$ for exactly one sign combination.

But if $\epsilon_1\sqrt{r_1} + \epsilon_2\sqrt{r_2} + \epsilon_3\sqrt{r_3} = 0$, then also $-\epsilon_1\sqrt{r_1} - \epsilon_2\sqrt{r_2} - \epsilon_3\sqrt{r_3} = 0$, which is the same. So actually there's one combination that gives 0, but the "negation" also gives 0. So 0 would appear in at least 2 of the 8 combinations if it appears at all.

Wait, if $\sqrt{r_1} + \sqrt{r_2} - \sqrt{r_3} = 0$, then $-\sqrt{r_1} - \sqrt{r_2} + \sqrt{r_3} = 0$ as well. So 0 appears in exactly 2 of the 8 combinations (or possibly more).

So if 0 appears exactly twice in the 8 combinations, we have 2 combinations giving 0 and 6 giving non-zero values. The 6 non-zero values might be 3 pairs $\pm v_i$ or could have further collisions.

For exactly 7 distinct values: we need 0 to appear exactly twice (contributing 1 distinct value), and the remaining 6 values to be 6 distinct nonzero values (contributing 6 distinct values). Total: 7.

Alternatively, 0 could appear more than twice, or there could be other coincidences.

Let me think differently. The 8 values are $\epsilon_1 a + \epsilon_2 b + \epsilon_3 c$ where $a = \sqrt{r_1}, b = \sqrt{r_2}, c = \sqrt{r_3}$ (choosing some square root). Notice $a, b, c$ are nonzero complex numbers.

The 8 values can be grouped as:
$\pm(a+b+c)$
$\pm(a+b-c)$
$\pm(a-b+c)$
$\pm(-a+b+c)$

These are 4 pairs under negation.

For exactly 7 distinct values, exactly one of these pairs must be $\{0, 0\}$, i.e., one of the 4 expressions is 0, and the other 3 pairs are $\{v_i, -v_i\}$ with $v_i \neq 0$ and all 6 values distinct.

So exactly one of: $a+b+c=0$, $a+b-c=0$, $a-b+c=0$, $-a+b+c=0$ holds.

Note: $a+b+c=0$ and $a+b-c=0$ can't both hold (that would require $c=0$). Similarly for other pairs. So at most one can be zero... well actually we need to check if two can hold simultaneously.

If $a+b+c=0$ and $a+b-c=0$, then $2c=0$, impossible.
If $a+b+c=0$ and $a-b+c=0$, then $2b=0$, impossible.
If $a+b+c=0$ and $-a+b+c=0$, then $2a=0$, impossible.
So at most one of the four can be zero, which is good.

For exactly 7 distinct values, we need exactly one of the four to be zero, and the remaining three pairs to give 6 distinct values (no additional coincidences).

So the condition is: exactly one of $a \pm b \pm c = 0$ (with an even or odd number of minus signs... let me re-examine).

Actually the four expressions (up to sign) are:
$a+b+c$, $a+b-c$, $a-b+c$, $a-b-c = -(a+b-c)$... wait that's not right.

The 8 values with 4 pairs are:
$+(a+b+c)$ and $-(a+b+c)$: pair 1
$+(a+b-c)$ and $-(a+b-c)$: pair 2
$+(a-b+c)$ and $-(a-b+c)$: pair 3
$+(a-b-c) = -(−a+b+c)$ and $-(a-b-c) = (-a+b+c)$: pair 4

For exactly 7 distinct values, we need exactly one pair to have value 0 (i.e., one of the four expressions $a+b+c$, $a+b-c$, $a-b+c$, $a-b-c$ equals 0).

Now, $a-b-c = 0$ iff $-a+b+c = 0$ iff one of the 8 values is 0. So WLOG if one of $a+b+c, a+b-c, a-b+c, a-b-c$ is zero.

Note: $a, b, c$ are square roots of the roots $r_1, r_2, r_3$ of the cubic. The choice of square root matters, but since we can choose $a = \sqrt{r_1}$ vs $-\sqrt{r_1}$, etc., and we're looking at all 8 combinations, the value of "one of the 4 expressions is zero" is independent of our choice of $a, b, c$ (since we're taking all sign combinations).

OK so the question is: for which values of $n$ is exactly one of $a+b+c$, $a+b-c$, $a-b+c$, $a-b-c$ equal to zero (where $a^2 = r_1, b^2 = r_2, c^2 = r_3$)?

$a+b+c = 0 \Leftrightarrow (a+b+c)^2 = 0 \Leftrightarrow r_1+r_2+r_3 + 2(ab+bc+ca) = 0$
But we need more care since $a+b+c=0$ doesn't mean $(a+b+c)^2 = 0$ necessarily gives back $a+b+c=0$... actually $(a+b+c)^2 = 0$ does imply $a+b+c=0$ if we're working over $\mathbb{C}$.

Hmm, let me use $e_1 = r_1+r_2+r_3 = n/6$, $e_2 = r_1r_2+r_2r_3+r_3r_1 = n-11$, $e_3 = r_1r_2r_3 = 400$.

Let $S = \epsilon_1 a + \epsilon_2 b + \epsilon_3 c$. Then $S = 0$ iff $S^2 = 0$ (over $\mathbb{C}$ this isn't automatically true... actually over $\mathbb{C}$, $S=0$ iff $S^2=0$).

$S^2 = r_1 + r_2 + r_3 + 2(\epsilon_1\epsilon_2 ab + \epsilon_2\epsilon_3 bc + \epsilon_1\epsilon_3 ac)$
$= e_1 + 2(\epsilon_1\epsilon_2 ab + \epsilon_2\epsilon_3 bc + \epsilon_1\epsilon_3 ac)$

Let $\delta_1 = \epsilon_2\epsilon_3, \delta_2 = \epsilon_1\epsilon_3, \delta_3 = \epsilon_1\epsilon_2$ (each $\pm 1$).

Then $S^2 = e_1 + 2(\delta_3 ab + \delta_1 bc + \delta_2 ac)$.

The four distinct cases (up to overall sign of $S$) correspond to:
1. $\delta_1=\delta_2=\delta_3=1$: $S^2 = e_1 + 2(ab+bc+ca)$
2. $\delta_1=1, \delta_2=\delta_3=-1$ (change sign of $a$): $S^2 = e_1 + 2(bc - ab - ac) = e_1 + 2(bc - a(b+c))$

Hmm, this is getting complicated. Let me try a different approach.

The condition "exactly one of the four expressions is zero" means:

One of $a+b+c, a+b-c, a-b+c, a-b-c = 0$.

This means one of $(\pm a \pm b \pm c)^2 = 0$ where not all signs are the same... actually all 8 choices but grouped.

$(\pm a \pm b \pm c) = 0$: note that these 8 expressions form 4 pairs by sign. For exactly one pair to be zero...

Let me think in terms of the elementary symmetric polynomials of $a, b, c$.

Let $p = a+b+c$, $q = ab+bc+ca$, $r = abc$.

$p^2 = a^2+b^2+c^2 + 2q = e_1 + 2q$
$(a+b-c)^2 = a^2+b^2+c^2 + 2ab - 2ac - 2bc = e_1 + 2(ab - ac - bc) = e_1 + 2(ab - c(a+b))$

Hmm. Let me consider $(a+b+c)(a+b-c)(a-b+c)(-a+b+c)$.

This equals $[(a+b+c)(-a+b+c)][(a+b-c)(a-b+c)]$... let me try another grouping.

$(a+b+c)(a+b-c) = (a+b)^2 - c^2 = a^2 + 2ab + b^2 - c^2$
$(a-b+c)(-a+b+c) = -(a-b-c)(a-b+c)$... hmm.

Actually there's a nice identity:
$(a+b+c)(-a+b+c)(a-b+c)(a+b-c) = 2(a^2b^2 + b^2c^2 + c^2a^2) - (a^4 + b^4 + c^4)$

Hmm, I know that $(a+b+c)(-a+b+c)(a-b+c)(a+b-c) = 2b^2c^2 + 2c^2a^2 + 2a^2b^2 - a^4 - b^4 - c^4$.

Actually $(-a+b+c)(a+b+c) = (b+c)^2 - a^2 = b^2 + 2bc + c^2 - a^2$

$(a-b+c)(a+b-c) = a^2 - (b-c)^2 = a^2 - b^2 + 2bc - c^2$

Product: $[(b+c)^2 - a^2][a^2 - (b-c)^2]$

Let $u = (b+c)^2, v = a^2, w = (b-c)^2$.

Product = $(u - v)(v - w) = uv - uw - v^2 + vw$

Hmm this is getting messy.

Let me try a cleaner approach. The product of all four is:
$P = (a+b+c)(a+b-c)(a-b+c)(a-b-c)$
$= [(a+b)^2-c^2][a^2-(b+c)^2]$... 

Wait, $(a+b+c)(a+b-c) = (a+b)^2 - c^2$
$(a-b+c)(a-b-c) = (a-b)^2 - c^2$... no wait: $(a-b+c)(a-b-c) = (a-b)^2 - c^2$.

Hmm, but $(a-b-c) = -(b+c-a) = -(b-a+c)$.

Actually I think I should approach this differently.

The product of all 8 values $\epsilon_1 a + \epsilon_2 b + \epsilon_3 c$ (for all sign combinations) equals $\pm(a^8 - ...)$... this might be complicated.

Let me go back to my original approach.

From Vieta for the cubic with roots $r_1 = \alpha^2, r_2 = \beta^2, r_3 = \gamma^2$:
- $r_1 + r_2 + r_3 = n/6$
- $r_1r_2 + r_2r_3 + r_3r_1 = n-11$
- $r_1r_2r_3 = 400$

Let $s = \alpha + \beta + \gamma$, $p = \alpha\beta + \beta\gamma + \gamma\alpha$, $q = \alpha\beta\gamma = \pm 20$.

Then:
- $s^2 - 2p = r_1 + r_2 + r_3 = n/6$, so $p = (s^2 - n/6)/2$
- $p^2 - 2sq = r_1r_2 + r_2r_3 + r_3r_1 = n-11$, so $p^2 = n - 11 + 2sq$

From these: $\left(\frac{s^2 - n/6}{2}\right)^2 = n - 11 + 2sq$

$(s^2 - n/6)^2 = 4(n-11) + 8sq$

Let me denote $q = \pm 20$ and expand:

$s^4 - \frac{n}{3}s^2 + \frac{n^2}{36} = 4(n-11) + 8sq$

$s^4 - \frac{n}{3}s^2 - 8qs + \frac{n^2}{36} - 4(n-11) = 0$

For $q = 20$: $s^4 - \frac{n}{3}s^2 - 160s + \frac{n^2}{36} - 4n + 44 = 0$ ... (I)
For $q = -20$: $s^4 - \frac{n}{3}s^2 + 160s + \frac{n^2}{36} - 4n + 44 = 0$ ... (II)

Note that (II) is obtained from (I) by $s \mapsto -s$.

So if $s_0$ is a root of (I), then $-s_0$ is a root of (II).

The set of all possible values of $\alpha + \beta + \gamma$ is the union of roots of (I) and (II).

If $\{s_1, s_2, s_3, s_4\}$ are roots of (I), then $\{-s_1, -s_2, -s_3, -s_4\}$ are roots of (II).

The union of roots is $\{s_1, s_2, s_3, s_4, -s_1, -s_2, -s_3, -s_4\}$.

For exactly 7 distinct values in this union, exactly one of $s_i = -s_j$ for some $i, j$ (giving a collapse), and no other collapses.

Case 1: $s_i = s_i$ for some $i$ (i.e., $s_i = -s_i$, so $s_i = 0$). This means 0 is a root of (I) and also 0 is a root of (II). Then the 8 values become $\{0, s_1, s_2, s_3, 0, -s_1, -s_2, -s_3\}$ = $\{0, s_1, s_2, s_3, -s_1, -s_2, -s_3\}$ = 7 values if $s_1, s_2, s_3, -s_1, -s_2, -s_3$ are all distinct and nonzero.

Case 2: $s_i = -s_j$ for $i \neq j$. This means some root of (I) is the negative of a different root of (I). Say $s_1 = -s_2$ (and $s_1 \neq 0$). Then $-s_1 = s_2$ is a root of (II). So the roots of (I) are $\{s_1, -s_1, s_3, s_4\}$ and roots of (II) are $\{-s_1, s_1, -s_3, -s_4\}$. The union is $\{s_1, -s_1, s_3, s_4, -s_3, -s_4\}$, which is 6 values (if all distinct). That's not 7.

Hmm, so Case 2 gives 6 distinct values.

Wait, let me redo. If the roots of (I) are $s_1, s_2, s_3, s_4$, then the roots of (II) are $-s_1, -s_2, -s_3, -s_4$.

The total set is $\{s_1, s_2, s_3, s_4\} \cup \{-s_1, -s_2, -s_3, -s_4\}$.

If all 8 are distinct, we get 8 values.
If exactly one coincidence: 7 values. This happens when $s_i = -s_j$ for exactly one pair $(i,j)$.
- If $s_i = -s_i$ (i.e., $s_i = 0$), then 0 appears once in each set, giving 7 values.
- If $s_i = -s_j$ for $i \neq j$, then $s_j$ is in the first set and $-s_j = s_i$ is in the first set, AND $-s_i = s_j$ is in the second set and $-s_j$ is in the second set too... wait.

Actually, if $s_1 = -s_2$ (nonzero), then $-s_2$ is in the first set (as $s_1$), and $s_2$ is also in the first set. So in the second set, $-s_1 = s_2$ is there, and $-s_2 = s_1$ is there. So the overlap between the first and second sets includes both $s_1 = -s_2$ (first set contains $s_1$, second set contains $-s_2 = s_1$) and $s_2 = -s_1$ (first set contains $s_2$, second set contains $-s_1 = s_2$). So we have 2 coincidences, giving $8 - 2 = 6$ distinct values.

So for exactly 7 coincidences, we need exactly one: $s_i = 0$ for exactly one $i \in \{1,2,3,4\}$, and no other coincidences.

This means 0 is a simple root of (I) (and consequently also a root of (II)).

So we need: 0 is a root of (I), 0 is not a repeated root, and no $s_i + s_j = 0$ for $i \neq j$ (where $s_1 = 0, s_2, s_3, s_4$ are roots of (I)) — well, $s_1 = 0$ so $-s_1 = 0$ which is back to $s_1$; for $i,j \geq 2$ with $i \neq j$, we need $s_i \neq -s_j$, and also $s_i \neq 0$ for $i = 2,3,4$.

Wait, also we need no $s_i = -s_i$ for $i \geq 2$, i.e., $s_2, s_3, s_4 \neq 0$. And no other pairs: $s_i \neq -s_j$ for distinct $i,j \in \{1,2,3,4\}$ except when one of them is 0 (but $0 = -0$ already counted).

OK so the condition is: 0 is a simple root of (I) (equivalently, 0 is a simple root of (II) since (II) is (I) under $s \to -s$), and the three nonzero roots $s_2, s_3, s_4$ of (I) satisfy $s_i \neq -s_j$ for all $i, j \in \{2,3,4\}$ (including $i = j$, i.e., $s_i \neq 0$) and $s_i \neq 0$.

For 0 to be a root of (I):
Plugging $s = 0$ into (I): $\frac{n^2}{36} - 4n + 44 = 0$
$n^2 - 144n + 1584 = 0$
$n = \frac{144 \pm \sqrt{144^2 - 4 \cdot 1584}}{2} = \frac{144 \pm \sqrt{20736 - 6336}}{2} = \frac{144 \pm \sqrt{14400}}{2} = \frac{144 \pm 120}{2}$

$n = 132$ or $n = 12$.

For 0 to be a simple root, we need $\frac{d}{ds}(\text{(I)})$ evaluated at $s = 0$ to be nonzero:
$\frac{d}{ds}(s^4 - \frac{n}{3}s^2 - 160s + C)|_{s=0} = -160 \neq 0$. ✓ (always simple)

So for both $n = 132$ and $n = 12$, 0 is a simple root of (I).

Now we need to check: for $n = 132$ and $n = 12$, do the remaining roots $s_2, s_3, s_4$ of (I) (after dividing out $(s-0) = s$) give 6 distinct nonzero values $\{s_2, s_3, s_4, -s_2, -s_3, -s_4\}$?

If 0 is a root of (I), we can factor:
(I)/$s$: $s^3 - \frac{n}{3}s - 160 = 0$ (since $C = 0$ when $n = 132$ or $n = 12$).

Wait let me redo. If $C = \frac{n^2}{36} - 4n + 44 = 0$, then (I) becomes:
$s^4 - \frac{n}{3}s^2 - 160s = 0$
$s(s^3 - \frac{n}{3}s - 160) = 0$

So the remaining roots satisfy $s^3 - \frac{n}{3}s - 160 = 0$.

For $n = 132$: $s^3 - 44s - 160 = 0$.
For $n = 12$: $s^3 - 4s - 160 = 0$.

For exactly 7 distinct values, we need the 6 values $\{s_2, s_3, s_4, -s_2, -s_3, -s_4\}$ to be distinct. This fails if:
1. Some $s_i = 0$ (but then $s_i$ would be a root of both $s^3 - \frac{n}{3}s - 160 = 0$ and $s = 0$, which would require $-160 = 0$, impossible). So no $s_i = 0$. ✓
2. Some $s_i = -s_j$ for $i \neq j$: then $-s_j$ is also a root of $s^3 - \frac{n}{3}s - 160 = 0$. If $s_j$ is a root, then $-s_j$ is also a root iff $-s_j$ satisfies $s^3 - \frac{n}{3}s - 160 = 0$, i.e., $(-s_j)^3 - \frac{n}{3}(-s_j) - 160 = 0 \Rightarrow -s_j^3 + \frac{n}{3}s_j - 160 = 0$. But $s_j^3 - \frac{n}{3}s_j - 160 = 0$, so adding: $-2 \cdot 160 = 0$, i.e., $-320 = 0$, contradiction. So no root and its negative can both be roots of the cubic. ✓
```

Ground truth: model reports greatest n = 132 (also finds n = 12).

Cost: send $0.20973 + reverse $0.214173 · 439.9s.
