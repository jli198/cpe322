# Lab 1 - GHDL and GTKWave

* Go to the GitHub repository of Digital System Design (DSD)
  * Study VHDL and GHDL
* Go to the GHDL folder
  * Install GHDL and GTKWave
  * Run Half Adder Example
  * Run another example such as D Flip-Flop or 4-to-1 Multiplexer
  * Document results on your GitHub repository
* Exploration: [Icarus Verilog](https://en.wikipedia.org/wiki/Icarus_Verilog)

## Installing GHDL and GTKWave

For simplicity sake, [Ubuntu was installed](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview) via [Windows Subsytem for Linux (WSL)](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux). It was not that hard of an installation process! </br>
</br>

The GHDL folder can be accessed by typing:

```sh
cd ghdl
```

The command cd changes directory and will take us into the ghdl folder. </br>
</br>

The following commands were inputted and some of the outputs are recorded below.

```sh
$ cat /etc/os-release
PRETTY_NAME="Ubuntu 22.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.1 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy

$ sudo apt update
$ sudo apt install gtkwave
$ sudo apt install git make gnat zlib1g-dev
$ git clone https://github.com/ghdl/ghdl
$ cd ghdl

$ ./configure --prefix=/usr/local
gcc (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

$ make
Use full IEEE library
Build machine is: x86_64-linux-gnu
create pic/ subdirectory
Creating Makefile
Creating default_paths.ads
Creating ghdl.gpr
Creating scripts/gcc/Make-lang.in
for d in ieee/v87 ieee/v93 ieee/v08 std/v87 std/v93 std/v08 src/ieee src/ieee/v87 src/ieee/v93 src/ieee2008 src/std src/std/v87 src/std/v93 src/std/v08 src/synopsys src/synopsys/v08 src/upf src/vital95 src/vital2000; do \
  mkdir -p lib/ghdl/$d; \
done
Generate ortho_code-x86-flags.ads
Generate elf_arch.ads
Generate ghdlsynth_maybe.ads
Generate grt-readline.ads

$ sudo make install
```

The DSD repo was cloned and the contents inside the vhdl folder were copied into a local folder using these commands.

```sh
$ git clone https://github.com/kevinwlu/dsd.git
$ mkdir vhdl
$ cd vhdl
$ cp ~/dsd/ghdl/*vhdl .
```

**Fun Fact:** * is an indicator for file extensions. So it's copying all the files in the ghdl folder with the .vhdl file extension into our newly minted vhdl folder.

![Terminal Results](installVHDL.jpg)

## Hello World

Let's try to print "Hello world!" The following commands were inputted and the resulting output is attached.

```sh
$ ghdl -h
$ ghdl -v
$ ghdl -a hello.vhdl
$ ghdl -e hello_world
$ ghdl -r hello_world
Hello world!
```

![Hello World](helloworld.jpg)

**It works!!**

## Adder

[Adder](https://en.wikipedia.org/wiki/Adder_(electronics)) </br>
An adder is a digital circuit in the arithmetic logic unit (ALU) that adds numbers. It is used in processors where addresses, table indicies, and increment + decrement counters need to be calculated.

### What is a Half-Adder?

[Half-Adder](https://en.wikipedia.org/wiki/Adder_(electronics)#Half_adder) </br>
The half adder adds two single binary digits **A** and **B** (only 1 bit). It results in sum (S) and carry (C) outputs. Carry is an overflow (like when you carry the 1).

### Running Half-Adder in GTKWave

The following commands were inputted and the resulting digital signal is attached.

```sh
$ ghdl -a ha.vhdl
$ ghdl -a ha_tb.vhdl
$ ghdl -e ha_tb
$ ghdl -r ha_tb --vcd=ha.vcd
ha_tb.vhdl:47:5:@5ns:(assertion error): Reached end of test
$ sudo gtkwave ha.vcd
GTKWave Analyzer v3.3.104 (w)1999-2020 BSI

[0] start time.
[5000000] end time.
```

Note: Because the Ubuntu instance used in this demo is not in a root directory, running gtkwave displays this message but the application still runs:

```sh
(gtkwave:7117): dconf-WARNING **: 17:59:37.128: failed to commit changes to dconf: Could not connect: No such file or directory
```

If affected, put sudo before any gtkwave command. </br>
</br>
When the app opens, one can see the SST tab and the entity ha_tb on the left. Click on this to see the entity half_addr. Right click on half_addr and Select either Append, Insert, or Replace inside the Recurse Import option. </br>
</br>
There is also a tab in the lower left with Type and Signals when the parent entity is clicked on. One can select these components (with the control key) and add the entities to the graph that way. </br>
</br>
After importing half_addr, there may not be anything. To see the whole digital signal, hold control and use the scroll wheel to scroll until the signal can be fully seen.

![Half Adder Signal](halfAdder.jpg)

### What is a Full-Adder?

[Full-Adder](https://en.wikipedia.org/wiki/Adder_(electronics)#Full_adder) </br>
A full adder allows for overflow outputs to act as an input and is useful for cascading adders when going up bits (8, 16, 32, etc). One application can be for custom transistor circuits.

### Running Full-Adder in GTKWave

The following commands were inputted and the resulting digital signal is attached.

```sh
$ ghdl -a adder.vhdl
$ ghdl -a adder_tb.vhdl
$ ghdl -e adder_tb
$ ghdl -r adder_tb --vcd=adder.vcd
adder_tb.vhdl:54:5:@8ns(assertion note): end of test
$ gtkwave adder.vcd
GTKWave Analyzer v3.3.104 (w)1999-2020 BSI

[0] start time.
[8000000] end time.
```

Make sure to follow the steps in the Half Adder example to see the full digital signal. The entities will have different names, but the process will be the same.*</br>
</br>
*Note: I had to rearrange the signals after importing to match what was on the DSD repo.

![Full-Adder Signal](fullAdder.jpg)

## Flip-Flop

[Flip-flop](https://en.wikipedia.org/wiki/Flip-flop_(electronics)) </br>
Flip-flops are circuits with 2 states that stores states. It is essential for digital electronics and are the storage mechanisms for a single bit of data ("on" or "off"; "1", or "0"; etc).

### What is a D Flip-Flop?

[D Flip-flop](https://www.analog.com/en/design-center/glossary/d-flip-flop.html#:~:text=A%20D%20(or%20Delay)%20Flip%20Flop,is%20shown%20in%20Figure%202.) </br>
D (or Delay) Flip-Flops delay the change of state of its outut signal until the input signal is triggered in its next cycle. It is used for memory espeically when shifting registers.

### Running D Flip-Flop in GTKWave

The following commands were inputted and the resulting digital signal is attached.

```sh
$ ghdl -a dff.vhdl
$ ghdl -a dff_tb.vhdl
$ ghdl -e dff_tb
$ sudo ghdl -r dff_tb --vcd=dff.vcd
$ sudo gtkwave dff.vcd
GTKWave Analyzer v3.3.104 (w)1999-2020 BSI

[0] start time.
[210000000] end time
```

Note: When running `ghdl -r dff_tb --vcd=dff.vcd`, the file may not be able to open: `ghdl:error: cannot open dff.vcd`. Try putting sudo before the command. </br>
Make sure to follow the steps in the Half Adder example to see the full digital signal. The entities will have different names, but the process will be the same.

![D Flip-Flop Signal](dff.jpg)

### What is a T Flip-Flop?

[T Flip-flop](https://en.wikipedia.org/wiki/Flip-flop_(electronics)#T_flip-flop) </br>
T (or Toggle) Flip-Flops allow for switching on and off. This can be useful in simplest terms to simulate pushing a button. In fact, the author's first exposure to T flip-flops were in Minecraft where they were used as a substitute for buttons in Redstone circuitry.

### Running T Flip-Flop in GTKWave

The following commands were inputted and the resulting digital signal is attached.

```sh
$ ghdl -a tff.vhdl
$ ghdl -a tff_tb.vhdl
$ ghdl -e tff_tb
$ ghdl -r tff_tb --vcd=tff.vcd
$ gtkwave tff.vcd
GTKWave Analyzer v3.3.104 (w)1999-2020 BSI

[0] start time.
[210000000] end time
```

Make sure to follow the steps in the Half Adder example to see the full digital signal. The entities will have different names, but the process will be the same.

![T Flip-Flop Signal](tff.jpg)

## Multiplexer

[Multiplexer](https://en.wikipedia.org/wiki/Multiplexer) </br>
A multiplexer decides between analog or digital inputs and forwards a selected input to a single output. Several inputs can be in a device especially those like [analog-to-digital converters](https://en.wikipedia.org/wiki/Analog-to-digital_converter). One use of the multiplexer is in computer networks.

### What is a 4-to-1 Multiplexer?

[4-to-1 Multiplexer](https://allaboutfpga.com/vhdl-4-to-1-mux-multiplexer) </br>
 A 4-to-1 mux has four inputs and one output.

### Running 4-to-1 Multiplexer in GTKWave

The following commands were inputted and the resulting digital signal is attached.

```sh
$ ghdl -a mux.vhdl
$ ghdl -a mux_tb.vhdl
$ ghdl -e mux_tb
$ ghdl -r mux_tb --vcd=mux.vcd
$ sudo gtkwave mux.vcd
GTKWave Analyzer v3.3.104 (w)1999-2020 BSI

[0] start time.
[500000000] end time.
```

Make sure to follow the steps in the Half Adder example to see the full digital signal. The entities will have different names, but the process will be the same.

![4-to-1 Multiplexer Signal](mux.jpg)

### What is a 1-to-4 Demultiplexer?

[1-to-4 Demultiplexer](https://allaboutfpga.com/vhdl-code-for-1-to-4-demux) </br>
 A 4-to-1 mux has one input and four outputs.

### Running 1-to-4 Demultiplexer in GTKWave

The following commands were inputted and the resulting digital signal is attached.

```sh
$ ghdl -a demux.vhdl
$ ghdl -a demux_tb.vhdl
$ ghdl -e demux_tb
$ ghdl -r demux_tb --vcd=demux.vcd
$ gtkwave demux.vcd
GTKWave Analyzer v3.3.104 (w)1999-2020 BSI

[0] start time.
[500000000] end time.
```

Make sure to follow the steps in the Half Adder example to see the full digital signal. The entities will have different names, but the process will be the same.*</br>
</br>
*Note: I had to rearrange the f signal to be at the bottom to match the repo.

![1-to-4 Demultiplexer Signal](demux.jpg)

## SR Flip-flop

[SR Flip-flop](https://en.wikipedia.org/wiki/Flip-flop_(electronics)#SR_NOR_latch) </br>
SR Flip-flop stands for "set-reset". One of the uses is the SR (or **RS**) NOR latch in which the output of the S gate can be used as an input to the R gate. When the R gate is activated (or reset), its output feeds into one of the inputs of the S gate, thus repeating the cycle whenever one activates the circuit. This has been used in Minecraft via [redstone circuitry](https://minecraft.fandom.com/wiki/Redstone_circuits/Memory). It is useful for applications in Minecraft such as button selectors.

### Running SR Flip-flop in GTKWave

The following commands were inputted and the resulting digital signal is attached.

```sh
$ ghdl -a --ieee=synopsys sr_ff.vhdl
$ ghdl -a --ieee=synopsys sr_ff_tb.vhdl
$ ghdl -e --ieee=synopsys sr_ff_tb
$ ghdl -r --ieee=synopsys sr_ff_tb --stop-time=100ns --vcd=sr_ff.vcd
$ sudo gtkwave sr_ff.vcd
GTKWave Analyzer v3.3.104 (w)1999-2020 BSI

[0] start time.
[100000000] end time.
```

Make sure to follow the steps in the Half Adder example to see the full digital signal. The entities will have different names, but the process will be the same.

![SR Flip-flop Signal](sr_ff.jpg)

## 8-bit Square Root

[8-bit Square Root](https://redirect.cs.umbc.edu/portal/help/VHDL/samples/samples.shtml#sqrt8) </br>
It takes in an 8-bit integer and outputs a 4-bit integer. It lowers the input by a factor of 2.

### Running 8-bit Square Root in GTKWave

The following commands were inputted and the resulting digital signal is attached.

```sh
$ ghdl -a --ieee=synopsys sqrt8.vhdl
sqrt8.vhdl:95:19:warning: declaration of "p" hides signal "p" [-Whide]
  procedure print(P : std_logic_vector(7 downto 0);
                  ^
sqrt8.vhdl:96:19:warning: declaration of "u" hides signal "u" [-Whide]
                  U : std_logic_vector(3 downto 0)) is
                  ^
$ ghdl -e --ieee=synopsys sqrt8
$ ghdl -r --ieee=synopsys sqrt8 --stop-time=512ns > sqrt8.out
$ cat sqrt8.out
ghdl:info: simulation stopped by --stop-time @512ns
$ ghdl -r --ieee=synopsys sqrt8 --stop-time=512ns --vcd=sqrt8.vcd
ghdl:info: simulation stopped by --stop-time @512ns
$ sudo gtkwave sqrt8.vcd
GTKWave Analyzer v3.3.104 (w)1999-2020 BSI

[0] start time.
[512000000] end time.
```

Make sure to follow the steps in the Half Adder example to see the full digital signal. The entities will have different names, but the process will be the same.*</br>
</br>
*Note: there's more than what's in the screenshot.

![8-bit Square Root Signal](sqrt8.jpg)

## References

[GHDL README.md in DSD GitHub Repo](https://github.com/kevinwlu/dsd/tree/master/ghdl)
