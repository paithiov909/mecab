//------------------------------------------------------------------------------
// <auto-generated />
//
// This file was automatically generated by SWIG (https://www.swig.org).
// Version 4.2.1
//
// Do not make changes to this file unless you know what you are doing - modify
// the SWIG interface file instead.
//------------------------------------------------------------------------------

namespace MeCab {

public class DictionaryInfo : global::System.IDisposable {
  private global::System.Runtime.InteropServices.HandleRef swigCPtr;
  protected bool swigCMemOwn;

  internal DictionaryInfo(global::System.IntPtr cPtr, bool cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = new global::System.Runtime.InteropServices.HandleRef(this, cPtr);
  }

  internal static global::System.Runtime.InteropServices.HandleRef getCPtr(DictionaryInfo obj) {
    return (obj == null) ? new global::System.Runtime.InteropServices.HandleRef(null, global::System.IntPtr.Zero) : obj.swigCPtr;
  }

  internal static global::System.Runtime.InteropServices.HandleRef swigRelease(DictionaryInfo obj) {
    if (obj != null) {
      if (!obj.swigCMemOwn)
        throw new global::System.ApplicationException("Cannot release ownership as memory is not owned");
      global::System.Runtime.InteropServices.HandleRef ptr = obj.swigCPtr;
      obj.swigCMemOwn = false;
      obj.Dispose();
      return ptr;
    } else {
      return new global::System.Runtime.InteropServices.HandleRef(null, global::System.IntPtr.Zero);
    }
  }

  ~DictionaryInfo() {
    Dispose(false);
  }

  public void Dispose() {
    Dispose(true);
    global::System.GC.SuppressFinalize(this);
  }

  protected virtual void Dispose(bool disposing) {
    lock(this) {
      if (swigCPtr.Handle != global::System.IntPtr.Zero) {
        if (swigCMemOwn) {
          swigCMemOwn = false;
          MeCabPINVOKE.delete_DictionaryInfo(swigCPtr);
        }
        swigCPtr = new global::System.Runtime.InteropServices.HandleRef(null, global::System.IntPtr.Zero);
      }
    }
  }

  public string filename {
    get {
      string ret = MeCabPINVOKE.DictionaryInfo_filename_get(swigCPtr);
      if (MeCabPINVOKE.SWIGPendingException.Pending) throw MeCabPINVOKE.SWIGPendingException.Retrieve();
      return ret;
    } 
  }

  public string charset {
    get {
      string ret = MeCabPINVOKE.DictionaryInfo_charset_get(swigCPtr);
      if (MeCabPINVOKE.SWIGPendingException.Pending) throw MeCabPINVOKE.SWIGPendingException.Retrieve();
      return ret;
    } 
  }

  public uint size {
    get {
      uint ret = MeCabPINVOKE.DictionaryInfo_size_get(swigCPtr);
      if (MeCabPINVOKE.SWIGPendingException.Pending) throw MeCabPINVOKE.SWIGPendingException.Retrieve();
      return ret;
    } 
  }

  public int type {
    get {
      int ret = MeCabPINVOKE.DictionaryInfo_type_get(swigCPtr);
      if (MeCabPINVOKE.SWIGPendingException.Pending) throw MeCabPINVOKE.SWIGPendingException.Retrieve();
      return ret;
    } 
  }

  public uint lsize {
    get {
      uint ret = MeCabPINVOKE.DictionaryInfo_lsize_get(swigCPtr);
      if (MeCabPINVOKE.SWIGPendingException.Pending) throw MeCabPINVOKE.SWIGPendingException.Retrieve();
      return ret;
    } 
  }

  public uint rsize {
    get {
      uint ret = MeCabPINVOKE.DictionaryInfo_rsize_get(swigCPtr);
      if (MeCabPINVOKE.SWIGPendingException.Pending) throw MeCabPINVOKE.SWIGPendingException.Retrieve();
      return ret;
    } 
  }

  public ushort version {
    get {
      ushort ret = MeCabPINVOKE.DictionaryInfo_version_get(swigCPtr);
      if (MeCabPINVOKE.SWIGPendingException.Pending) throw MeCabPINVOKE.SWIGPendingException.Retrieve();
      return ret;
    } 
  }

  public DictionaryInfo next {
    get {
      global::System.IntPtr cPtr = MeCabPINVOKE.DictionaryInfo_next_get(swigCPtr);
      DictionaryInfo ret = (cPtr == global::System.IntPtr.Zero) ? null : new DictionaryInfo(cPtr, false);
      if (MeCabPINVOKE.SWIGPendingException.Pending) throw MeCabPINVOKE.SWIGPendingException.Retrieve();
      return ret;
    } 
  }

  public DictionaryInfo() : this(MeCabPINVOKE.new_DictionaryInfo(), true) {
    if (MeCabPINVOKE.SWIGPendingException.Pending) throw MeCabPINVOKE.SWIGPendingException.Retrieve();
  }

}

}
