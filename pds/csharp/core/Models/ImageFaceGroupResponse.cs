// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 
     */
    public class ImageFaceGroupResponse : TeaModel {
        /// <summary>
        /// cover_file_id
        /// </summary>
        [NameInMap("cover_file_id")]
        [Validation(Required=false)]
        public string CoverFileId { get; set; }

        /// <summary>
        /// 人脸分组生成时间
        /// </summary>
        [NameInMap("created_at")]
        [Validation(Required=false)]
        public string CreatedAt { get; set; }

        /// <summary>
        /// 人脸个数
        /// </summary>
        [NameInMap("face_count")]
        [Validation(Required=false)]
        public long FaceCount { get; set; }

        /// <summary>
        /// 人脸分组封面头像地址
        /// </summary>
        [NameInMap("group_cover_url")]
        [Validation(Required=false)]
        public string GroupCoverUrl { get; set; }

        /// <summary>
        /// 人脸分组 ID
        /// </summary>
        [NameInMap("group_id")]
        [Validation(Required=false)]
        public string GroupId { get; set; }

        /// <summary>
        /// 人脸分组名称
        /// </summary>
        [NameInMap("group_name")]
        [Validation(Required=false)]
        public string GroupName { get; set; }

        /// <summary>
        /// 照片个数
        /// </summary>
        [NameInMap("image_count")]
        [Validation(Required=false)]
        public long ImageCount { get; set; }

        /// <summary>
        /// 人脸分组修改时间
        /// </summary>
        [NameInMap("updated_at")]
        [Validation(Required=false)]
        public string UpdatedAt { get; set; }

    }

}
