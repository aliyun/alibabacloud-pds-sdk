// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 获取签名 response
     */
    public class OSSListUploadedPartResponse : TeaModel {
        /// <summary>
        /// file_path
        /// </summary>
        [NameInMap("file_path")]
        [Validation(Required=false)]
        public string FilePath { get; set; }

        /// <summary>
        /// next_part_number_marker
        /// </summary>
        [NameInMap("next_part_number_marker")]
        [Validation(Required=false)]
        public string NextPartNumberMarker { get; set; }

        /// <summary>
        /// upload_id
        /// </summary>
        [NameInMap("upload_id")]
        [Validation(Required=false)]
        public string UploadId { get; set; }

        /// <summary>
        /// uploaded_parts
        /// </summary>
        [NameInMap("uploaded_parts")]
        [Validation(Required=false)]
        public List<UploadPartInfo> UploadedParts { get; set; }

    }

}
