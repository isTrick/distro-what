d_mx = 'MX Linux'
p_mx = 0

d_mint = 'Mint'
p_mint = 0

d_endeavour = 'Endeavour'
p_endeavour = 0

d_debian = 'Debian'
p_debian = 0

d_manjaro = 'Manjaro'
p_manjaro = 0

d_ubuntu = 'Ubuntu'
p_ubuntu = 0

d_fedora = 'Fedora'
p_fedora = 0

d_popos = 'Pop!_OS'
p_popos = 0

d_opensuse = 'openSUSE'
p_opensuse = 0

d_zorin = 'Zorin'
p_zorin = 0

print('Responda 1 para sim e 0 para não')


q_experience = int(input("Você já teve experiência com Linux? "))
if q_experience != 1 or 0:
    print("Responda com 1 para sim ou 0 para não!")
    q_experience = input("Você já teve experiência com Linux? ")

if q_experience == 1:
    p_debian = p_debian + 1
    p_fedora = p_fedora + 1
    p_opensuse = p_opensuse + 1


q_ootb = int(input("Você costuma configurar seu próprio sistema? "))
if q_ootb != 1 or 0:
    print("Responda com 1 ou 0!")
    q_ootb = input("Você costuma configurar seu próprio sistema? ")

if q_ootb == 1:
    p_debian = p_debian + 1
    p_fedora = p_fedora + 1
    p_opensuse = p_opensuse + 1  


q_mainos = int(input("Você prefere windows do que MacOS? "))
if q_mainos != 1 or 0:
    print("Responda com 1 ou 0!")
    q_mainos = input("Você prefere windows do que MacOS? ")

if q_mainos == 1:
    p_zorin = p_zorin + 1
    p_mint = p_mint + 1

q_releases = int(input("Você prefere estabilidade do que novidades? "))
if q_releases != 1 or 0:
   print("Responda com 1 ou 0!")

if q_releases == 1:
    p_debian = p_debian + 1
    p_zorin = p_zorin + 1
    p_mint = p_mint + 1
    p_ubuntu = p_ubuntu + 1


name = input("Qual o seu nome? ")


results = [p_debian, p_endeavour, p_fedora, p_manjaro, p_mint, p_mx, p_ubuntu, p_zorin, p_popos, p_opensuse]


if results[0] == p_debian:
    print(f'{name}, sua distro perfeita é o {d_debian}')


