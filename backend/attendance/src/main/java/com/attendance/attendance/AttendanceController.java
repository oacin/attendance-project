package com.attendance.attendance;

import java.util.ArrayList;
import java.util.List;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@CrossOrigin
@RestController
public class AttendanceController {
  private List<Attendance> attendances = new ArrayList<>();

  @GetMapping("/attendances")
  public List<Attendance> toList() {
    return attendances;
  }
  
  @PostMapping("/attendances")
  public String save(@RequestBody List<Attendance> attendanceList) {
    this.attendances = attendanceList;

    return "saved";
  }
}
