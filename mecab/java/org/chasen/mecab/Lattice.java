/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (https://www.swig.org).
 * Version 4.2.0
 *
 * Do not make changes to this file unless you know what you are doing - modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package org.chasen.mecab;

public class Lattice {
  private transient long swigCPtr;
  protected transient boolean swigCMemOwn;

  protected Lattice(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(Lattice obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  protected static long swigRelease(Lattice obj) {
    long ptr = 0;
    if (obj != null) {
      if (!obj.swigCMemOwn)
        throw new RuntimeException("Cannot release ownership as memory is not owned");
      ptr = obj.swigCPtr;
      obj.swigCMemOwn = false;
      obj.delete();
    }
    return ptr;
  }

  @SuppressWarnings({"deprecation", "removal"})
  protected void finalize() {
    delete();
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        MeCabJNI.delete_Lattice(swigCPtr);
      }
      swigCPtr = 0;
    }
  }

  public void clear() {
    MeCabJNI.Lattice_clear(swigCPtr, this);
  }

  public boolean is_available() {
    return MeCabJNI.Lattice_is_available(swigCPtr, this);
  }

  public Node bos_node() {
    long cPtr = MeCabJNI.Lattice_bos_node(swigCPtr, this);
    return (cPtr == 0) ? null : new Node(cPtr, false);
  }

  public Node eos_node() {
    long cPtr = MeCabJNI.Lattice_eos_node(swigCPtr, this);
    return (cPtr == 0) ? null : new Node(cPtr, false);
  }

  public Node end_nodes(long pos) {
    long cPtr = MeCabJNI.Lattice_end_nodes(swigCPtr, this, pos);
    return (cPtr == 0) ? null : new Node(cPtr, false);
  }

  public Node begin_nodes(long pos) {
    long cPtr = MeCabJNI.Lattice_begin_nodes(swigCPtr, this, pos);
    return (cPtr == 0) ? null : new Node(cPtr, false);
  }

  public String sentence() {
    return MeCabJNI.Lattice_sentence(swigCPtr, this);
  }

  public long size() {
    return MeCabJNI.Lattice_size(swigCPtr, this);
  }

  public void set_Z(double Z) {
    MeCabJNI.Lattice_set_Z(swigCPtr, this, Z);
  }

  public double Z() {
    return MeCabJNI.Lattice_Z(swigCPtr, this);
  }

  public void set_theta(float theta) {
    MeCabJNI.Lattice_set_theta(swigCPtr, this, theta);
  }

  public float theta() {
    return MeCabJNI.Lattice_theta(swigCPtr, this);
  }

  public boolean next() {
    return MeCabJNI.Lattice_next(swigCPtr, this);
  }

  public int request_type() {
    return MeCabJNI.Lattice_request_type(swigCPtr, this);
  }

  public boolean has_request_type(int request_type) {
    return MeCabJNI.Lattice_has_request_type(swigCPtr, this, request_type);
  }

  public void set_request_type(int request_type) {
    MeCabJNI.Lattice_set_request_type(swigCPtr, this, request_type);
  }

  public void add_request_type(int request_type) {
    MeCabJNI.Lattice_add_request_type(swigCPtr, this, request_type);
  }

  public void remove_request_type(int request_type) {
    MeCabJNI.Lattice_remove_request_type(swigCPtr, this, request_type);
  }

  public Node newNode() {
    long cPtr = MeCabJNI.Lattice_newNode(swigCPtr, this);
    return (cPtr == 0) ? null : new Node(cPtr, false);
  }

  public String toString() {
    return MeCabJNI.Lattice_toString__SWIG_0(swigCPtr, this);
  }

  public String toString(Node node) {
    return MeCabJNI.Lattice_toString__SWIG_1(swigCPtr, this, Node.getCPtr(node), node);
  }

  public String enumNBestAsString(long N) {
    return MeCabJNI.Lattice_enumNBestAsString(swigCPtr, this, N);
  }

  public boolean has_constraint() {
    return MeCabJNI.Lattice_has_constraint(swigCPtr, this);
  }

  public int boundary_constraint(long pos) {
    return MeCabJNI.Lattice_boundary_constraint(swigCPtr, this, pos);
  }

  public String feature_constraint(long pos) {
    return MeCabJNI.Lattice_feature_constraint(swigCPtr, this, pos);
  }

  public void set_boundary_constraint(long pos, int boundary_constraint_type) {
    MeCabJNI.Lattice_set_boundary_constraint(swigCPtr, this, pos, boundary_constraint_type);
  }

  public void set_feature_constraint(long begin_pos, long end_pos, String feature) {
    MeCabJNI.Lattice_set_feature_constraint(swigCPtr, this, begin_pos, end_pos, feature);
  }

  public void set_result(String result) {
    MeCabJNI.Lattice_set_result(swigCPtr, this, result);
  }

  public String what() {
    return MeCabJNI.Lattice_what(swigCPtr, this);
  }

  public void set_what(String str) {
    MeCabJNI.Lattice_set_what(swigCPtr, this, str);
  }

  public Lattice() {
    this(MeCabJNI.new_Lattice(), true);
  }

  public void set_sentence(String sentence) {
    MeCabJNI.Lattice_set_sentence(swigCPtr, this, sentence);
  }

}
