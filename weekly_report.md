
## 4/21/2020

### Achievements

* A stable prototype telemetry protocol communication between RaspberryPi and Slave device via SPI (99.99% working)


### To Do

* Refactor code that handles recieving of SPI data on uC and create library that can be updated and reused throughout all firmware that requires uC
  to operate as slave.

* Create default struct in Master SPI that uses default MISO, MOSI, SCLK, CS pins and uses standard telemetry protocol

* Setup test scenerio where two slave devices are communicating with master device

### Problems

### Ideas
 
* Create a generic packet structure that can be reused between all communication devices.
* Switch communication protocol to I2C, instead of SPI?
