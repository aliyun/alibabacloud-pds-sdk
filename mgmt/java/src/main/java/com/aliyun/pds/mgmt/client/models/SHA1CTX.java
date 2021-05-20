// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 对应OSS Sha1的结构体，定义在 gitlab.alibaba-inc.com/oss/parallel_hash.go OSSSha1Digest
type OSSSha1Digest struct {
h   [5]uint32         // h是计算sha1时存放中间结果的变量，参与每一轮Sha1的计算，必不可少，最后的Sha1值也由这几个数字决定
x   [BlockSize]byte   // 上一轮计算非64字节对齐时，不足64节的内容会保存在这里
nx  int               // 上一轮计算数据长度取模64的结果，64字节对齐时这个值为0
len uint64            // 到上一个数据块为止的总长度，字节，用来计算 OSSRequestSha1Ctx 中的Nl, Nh
}

SHA1CTX 是 OSSSha1Digest 的简化
当每轮计算Sha1的数据长度为64位对齐时，nx固定为0，x长度为0，只需包含h和len；part_offset对应OSSSha1Digest的len
 */
public class SHA1CTX extends TeaModel {
    @NameInMap("h")
    public java.util.List<Integer> h;

    @NameInMap("part_offset")
    public Long partOffset;

    public static SHA1CTX build(java.util.Map<String, ?> map) throws Exception {
        SHA1CTX self = new SHA1CTX();
        return TeaModel.build(map, self);
    }

    public SHA1CTX setH(java.util.List<Integer> h) {
        this.h = h;
        return this;
    }
    public java.util.List<Integer> getH() {
        return this.h;
    }

    public SHA1CTX setPartOffset(Long partOffset) {
        this.partOffset = partOffset;
        return this;
    }
    public Long getPartOffset() {
        return this.partOffset;
    }

}
