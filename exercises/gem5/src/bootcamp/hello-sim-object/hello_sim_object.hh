#ifndef __BOOTCAMP_HELLO_SIM_OBJECT_HELLO_SIM_OBJECT_HH__
#define __BOOTCAMP_HELLO_SIM_OBJECT_HELLO_SIM_OBJECT_HH__

#include "bootcamp/hello-sim-object/goodbye_sim_object.hh"
#include "params/HelloSimObject.hh"
#include "sim/sim_object.hh"

namespace gem5
{

class HelloSimObject: public SimObject
{
  private:
    int remainingHellosToPrintByEvent;

    GoodByeSimObject* goodByeObject;
    EventFunctionWrapper nextHelloEvent;
    void processNextHelloEvent();
  public:
    virtual void startup() override;
    HelloSimObject(const HelloSimObjectParams& params);
};

} // namespace gem5

#endif // __BOOTCAMP_HELLO_SIM_OBJECT_HELLO_SIM_OBJECT_HH__
