p, v = map(int,input().split())
q, m = map(int,input().split())

if p > q:
    p, q = q, p # Маша всегда правее
    v, m = m, v

v_left = p - v
v_right = p + v

m_left = q - m
m_right = q + m

if v_right < m_left: # Множества не пересекаются
    print((v_right - v_left + 1) + (m_right - m_left + 1)) 
else:
    if v_left >= m_left: # Маша покрывает Васю
        print(m_right - m_left + 1)
    else:
        if v_right < m_right:
            print(m_right - v_left + 1) # Пересекаются
        else:
            print(v_right - v_left + 1) # Вася покрывает Машу