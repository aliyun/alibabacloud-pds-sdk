// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class StreamUploadInfo extends TeaModel {
    /**
     * <p>location</p>
     */
    @NameInMap("location")
    public String location;

    /**
     * <p>part_info_list</p>
     */
    @NameInMap("part_info_list")
    public java.util.List<UploadPartInfo> partInfoList;

    /**
     * <p>pre_rapid_upload</p>
     * <p>type: boolean</p>
     */
    @NameInMap("pre_rapid_upload")
    public Boolean preRapidUpload;

    /**
     * <p>rapid_upload</p>
     * <p>type: boolean</p>
     */
    @NameInMap("rapid_upload")
    public Boolean rapidUpload;

    /**
     * <p>upload_id</p>
     */
    @NameInMap("upload_id")
    public String uploadId;

    public static StreamUploadInfo build(java.util.Map<String, ?> map) throws Exception {
        StreamUploadInfo self = new StreamUploadInfo();
        return TeaModel.build(map, self);
    }

    public StreamUploadInfo setLocation(String location) {
        this.location = location;
        return this;
    }
    public String getLocation() {
        return this.location;
    }

    public StreamUploadInfo setPartInfoList(java.util.List<UploadPartInfo> partInfoList) {
        this.partInfoList = partInfoList;
        return this;
    }
    public java.util.List<UploadPartInfo> getPartInfoList() {
        return this.partInfoList;
    }

    public StreamUploadInfo setPreRapidUpload(Boolean preRapidUpload) {
        this.preRapidUpload = preRapidUpload;
        return this;
    }
    public Boolean getPreRapidUpload() {
        return this.preRapidUpload;
    }

    public StreamUploadInfo setRapidUpload(Boolean rapidUpload) {
        this.rapidUpload = rapidUpload;
        return this;
    }
    public Boolean getRapidUpload() {
        return this.rapidUpload;
    }

    public StreamUploadInfo setUploadId(String uploadId) {
        this.uploadId = uploadId;
        return this;
    }
    public String getUploadId() {
        return this.uploadId;
    }

}
