package com.attendance.attendance.controller;

import com.attendance.attendance.Return;
import com.attendance.attendance.model.Attendance;
import com.attendance.attendance.repository.AttendanceRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@CrossOrigin(origins = "*")
@RestController
public class AttendanceController {
  @Autowired
  AttendanceRepository repository;

  @GetMapping("/attendance")
  public Return findAll()
  {
    try {
      return new Return(repository.findAll());
    } catch (Exception e) {
      return new Return(e.getMessage());
    }
  }

  @PostMapping("/attendance")
  public Return add(@RequestBody Attendance attendance)
  {
    try {
      return new Return(repository.add(attendance));
    } catch (Exception e) {
      return new Return(e.getMessage());
    }
  }
}
