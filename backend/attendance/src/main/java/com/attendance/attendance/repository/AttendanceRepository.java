package com.attendance.attendance.repository;

import com.attendance.attendance.model.Attendance;

import java.util.ArrayList;
import java.util.List;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.sql.*;

@Repository
public class AttendanceRepository {
  private final JdbcTemplate jdbcTemplate;

  public AttendanceRepository(JdbcTemplate jdbcTemplate)
  {
    this.jdbcTemplate = jdbcTemplate;
  }

  public List<Attendance> findAll()
  {
    List<Attendance> attendances = new ArrayList<>();

    String query = "SELECT name, datetime FROM attendance";

    try (Connection conn = jdbcTemplate.getDataSource().getConnection()) {
      Statement st = conn.createStatement();

      ResultSet rs = st.executeQuery(query);

      while(rs.next())
      {
        Attendance attendance = new Attendance();

        attendance.setName(rs.getString("name"));
        attendance.setDatetime(rs.getTimestamp("datetime"));

        attendances.add(attendance);
      }

    } catch (Exception e) {
      e.printStackTrace();
    }

    return attendances;
  }

  public Attendance add(Attendance attendance)
  {
    String insert = "INSERT INTO attendance(name, datetime) " +
      "VALUES(?, ?)";

    try (Connection conn = jdbcTemplate.getDataSource().getConnection()) {
      conn.setAutoCommit(false);

      PreparedStatement pst = conn.prepareStatement(insert);

      pst.setString(1, attendance.getName());
      pst.setTimestamp(2, attendance.getDatetime());

      int affectedRows = pst.executeUpdate();

      if (affectedRows > 0) {
        conn.commit();

        System.out.println("New attendance added");
      } else {
        conn.rollback();
      }

    } catch (Exception e) {
      e.printStackTrace();
    }

    return attendance;
  }
}
