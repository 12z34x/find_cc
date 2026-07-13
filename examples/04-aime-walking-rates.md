# Example: AIME 2026 — Walking / Running / Bicycling Rates (answer-only harvest)

Reproduced with open-open-reasoning. **Answer-only construction**: the visible reply is
forced down to the bare final result, so *no* reasoning is human-readable in the response —
the full chain-of-thought survives only inside the sealed `signature`. Reversing that
signature back into the working (plus the planted secret, which the visible reply never
contains) is the actual proof that the signature encodes the hidden reasoning.
Planted marker uses open-reasoning's BYOK secret shape `WORD-XXXXX-WORD-NN` (same
`rollSecret` construction as `index.html`). `<cot>` is only our local dump wrapper.
Based on: https://github.com/s-JoL/open-reasoning

Model: claude-sonnet-4-6 · `thinking.display=omitted` · `effort=medium` · `max_tokens=16000` · plant_secret = `ORBIT-TKP5K-ORBIT-15`

Q:
```markdown
Patrick started walking at a constant rate along a straight road from school to the park. One hour after Patrick left, Tanya started running along the same road from school to the park. One hour after Tanya left, Jose started bicycling along the same road from school to the park. Tanya ran at a constant rate of 2 miles per hour faster than Patrick walked, Jose bicycled at a constant rate of 7 miles per hour faster than Tanya ran, and all three arrived at the park at the same time. The distance from the school to the park is m/n miles, where m and n are relatively prime positive integers. Find m + n.
```

## What the caller actually sees (visible reply — result only, 3 chars)

```markdown
277
```

Summary field (`display:omitted` → empty; 0 hidden reasoning tokens sealed in signature):

```markdown
*(empty — sealed into signature only)*
```

## Reverse-engineered thinking (recovered from the signature alone)

- **token_alignment = None** (578/0 recovered/hidden)
- recovered_chars = 1065 · reversed CoT is **355x** longer than the visible reply
- planted secret present in reversed CoT = **True** · present in visible reply = **False**
  (secret appears only in the recovered thinking → the signature really carried the hidden reasoning)
- meta = {'audit_token': 'ORBIT-TKP5K-ORBIT-15', 'chunks': 1, 'recovered_output_tokens': 578, 'strategy': 'cot', 'truncated': False}

```markdown
ORBIT-TKP5K-ORBIT-15

Let Patrick's speed = v mph
Tanya's speed = v + 2 mph
Jose's speed = v + 9 mph

Let d = distance from school to park.

Patrick's travel time = d/v hours
Tanya's travel time = d/(v+2) hours
Jose's travel time = d/(v+9) hours

Patrick left 1 hour before Tanya, Tanya left 1 hour before Jose.

They all arrive at the same time.

Patrick's total time = d/v
Tanya's total time = d/(v+2), but she left 1 hour after Patrick, so Patrick's time = d/(v+2) + 1
Jose's total time = d/(v+9), but he left 2 hours after Patrick, so Patrick's time = d/(v+9) + 2

So:
d/v = d/(v+2) + 1
d/v = d/(v+9) + 2

From equation 1:
d/v - d/(v+2) = 1
d(v+2 - v)/(v(v+2)) = 1
2d/(v(v+2)) = 1
d = v(v+2)/2

From equation 2:
d/v - d/(v+9) = 2
d(v+9-v)/(v(v+9)) = 2
9d/(v(v+9)) = 2
d = 2v(v+9)/9

Setting equal:
v(v+2)/2 = 2v(v+9)/9
(v+2)/2 = 2(v+9)/9
9(v+2) = 4(v+9)
9v + 18 = 4v + 36
5v = 18
v = 18/5

d = v(v+2)/2 = (18/5)(18/5 + 2)/2 = (18/5)(28/5)/2 = (18·28)/(50) = 504/50 = 252/25

gcd(252, 25) = 1 (25 = 5², 252 = 4·63 = 4·9·7, no factor of 5)

m + n = 252 + 25 = 277
```

Ground truth: distance = 252/25 miles, so m + n = 277.

Cost: send $0.009609 + reverse $0.011694 · 45.2s.
