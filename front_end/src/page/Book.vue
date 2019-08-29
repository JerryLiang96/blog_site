<template>
  <el-row>
    <el-col :span="18">
      <el-col :span="6" v-for="o in 6" :key="o" :offset=1>
        <el-card shadow="hover">
          <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
            class="image">
          <div style="padding: 14px;">
            <span>BOOK NAME</span>
          </div>
        </el-card>
      </el-col>
    </el-col>
    <el-col :span="6">
      <div class="grid-content bg-purple"></div>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name: 'Computer',
  data: () => ({
    show2: true
  })
}
</script>

<style>
.transition-box {
  margin-bottom: 10px;
  width: 200px;
  height: 100px;
  border-radius: 4px;
  background-color: #409eff;
  text-align: center;
  color: #fff;
  padding: 40px 20px;
  box-sizing: border-box;
  margin-right: 20px;
}
</style>
