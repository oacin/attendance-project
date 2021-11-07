package com.attendance.attendance.model;

import java.sql.Timestamp;

public class Attendance {
  private String name;
  private Timestamp datetime;

  public Attendance() {
  }

  public Attendance(String name, Timestamp datetime) {
    this.name = name;
    this.datetime = datetime;
  }

  public Timestamp getDatetime() {
    return this.datetime;
  }

  public void setDatetime(Timestamp datetime) {
    this.datetime = datetime;
  }

  public String getName() {
    return this.name;
  }

  public void setName(String name) {
    this.name = name;
  }
}
