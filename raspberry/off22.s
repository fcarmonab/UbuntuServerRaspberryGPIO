
@--Data sectionn
.data
.balign 4
pin: .int 22
OUTPUT = 1

@--Code Section
.text
.global main
.extern printf
.extern wiringPiSetup
.extern digitalWrite
.extern pinMode

main:   push {ip, lr}
     bl wiringPiSetup
     ldr r0, =pin
     ldr r0, [r0]
     mov r1, #OUTPUT
     bl pinMode
     @ digitalwrite {pin, 22}
     ldr r0, =pin
     ldr r0, [r0]
     mov r1, #0
     bl digitalWrite
pop      {ip, pc}
