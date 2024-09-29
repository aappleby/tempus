`default_nettype none
`timescale 1 ns/1 ns

module simple_sink
(
  input logic      clock,
  input logic      reset,

  input logic[7:0] src_data,
  input logic      src_valid,
  output logic     src_ready
);

  logic[7:0] data = 0;

  assign src_ready = 1;

  always @(posedge clock) begin
    if (reset) begin
      data <= 0;
    end else if (src_valid) begin
      data <= src_data;
    end
  end

endmodule
