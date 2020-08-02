# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import codec, CheckForError, api_util, Base


class IActiveClass(Base):
    __slots__ = []
    _api_prefix = "ActiveClass"
    _columns = ["ActiveClassName", "ActiveClassParent", "Name", "NumElements"]

    def ActiveClassName(self):
        """(read-only) Returns name of active class."""
        return self._get_string(
            self.CheckForError(self._lib.ActiveClass_Get_ActiveClassName())
        )

    def AllNames(self):
        """(read-only) Array of strings consisting of all element names in the active class."""
        return self.CheckForError(
            self._get_string_array(self._lib.ActiveClass_Get_AllNames)
        )

    def Count(self):
        """(read-only) Number of elements in Active Class. Same as NumElements Property."""
        return self.CheckForError(self._lib.ActiveClass_Get_Count())

    def First(self):
        """(read-only) Sets first element in the active class to be the active DSS object. If object is a CktElement, ActiveCktELment also points to this element. Returns 0 if none."""
        return self.CheckForError(self._lib.ActiveClass_Get_First())

    def Name(self, *args):
        """Name of the Active Element of the Active Class"""
        # Getter
        if len(args) == 0:
            return self._get_string(
                self.CheckForError(self._lib.ActiveClass_Get_Name())
            )

        # Setter
        Value, = args
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)
        self.CheckForError(self._lib.ActiveClass_Set_Name(Value))

    def Next(self):
        """(read-only) Sets next element in active class to be the active DSS object. If object is a CktElement, ActiveCktElement also points to this element.  Returns 0 if no more."""
        return self.CheckForError(self._lib.ActiveClass_Get_Next())

    def NumElements(self):
        """(read-only) Number of elements in this class. Same as Count property."""
        return self.CheckForError(self._lib.ActiveClass_Get_NumElements())

    def ActiveClassParent(self):
        """Get the name of the parent class of the active class"""
        return self._get_string(
            self.CheckForError(self._lib.ActiveClass_Get_ActiveClassParent())
        )


_ActiveClass = IActiveClass(api_util)

# For backwards compatibility, bind to the default instance
ActiveClassName = _ActiveClass.ActiveClassName
AllNames = _ActiveClass.AllNames
Count = _ActiveClass.Count
First = _ActiveClass.First
Name = _ActiveClass.Name
Next = _ActiveClass.Next
NumElements = _ActiveClass.NumElements
ActiveClassParent = _ActiveClass.ActiveClassParent
_columns = _ActiveClass._columns
__all__ = [
    "ActiveClassName",
    "AllNames",
    "Count",
    "First",
    "Name",
    "Next",
    "NumElements",
    "ActiveClassParent",
]
