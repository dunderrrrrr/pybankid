from typing import Literal, TypedDict, Any


class SignState(TypedDict):
    orderRef: str
    autoStartToken: str
    qrStartToken: str
    qrStartSecret: str


class AuthState(TypedDict):
    orderRef: str
    autoStartToken: str
    qrStartToken: str
    qrStartSecret: str


class PhoneAuthState(TypedDict):
    orderRef: str


class PhoneSignState(TypedDict):
    orderRef: str


class CollectState(TypedDict):
    orderRef: str
    status: Literal["pending", "failed", "complete"]
    hintCode: Literal["userSign", "userCancel", "complete"] | None
    completionData: dict[str, Any] | None