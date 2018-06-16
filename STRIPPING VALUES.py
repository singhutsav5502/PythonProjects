text = "X-DSPAM-Confidence:    0.8475";
colonPOS=text.find(':')
data = text[colonPOS+1 : ]
STRIPPED = data.strip()
floatVAL=float(STRIPPED)
print(floatVAL)
