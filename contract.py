from pyteal import *
from beaker import *

class DiplomaApp(Application):

  teacher = ApplicationStateValue(
    stack_type=TealType.bytes,
    default=Txn.sender(),
    descr="Teacher variable that stores the allowed user to create diplomas"
  )

  diploma = AccountStateValue(
    stack_type=TealType.bytes.bytes,
    descr="Diploma title for the student"
  )

  @create
  def create(self):
    return self.initialize_application_state()

  @opt_in
  def opt_in(self):
    return self.initialize_account_state()

  @external
  def change_teacher(self):
    return Seq([
      Assert(Txn.sender() == self.teacher),
      self.teacher.set(Txn.accounts[1])
    ])
  
  @external
  def register_diploma(self, title: abi.String):
    return Seq([
      Assert(Txn.sender() == self.teacher),
      self.diploma[Txn.accounts[1]].set(title.get())
    ])

  
