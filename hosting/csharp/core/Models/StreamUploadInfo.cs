// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 
     */
    public class StreamUploadInfo : TeaModel {
        /// <summary>
        /// part_info_list
        /// </summary>
        [NameInMap("part_info_list")]
        [Validation(Required=false)]
        public List<UploadPartInfo> PartInfoList { get; set; }

        /// <summary>
        /// pre_rapid_upload
        /// type: boolean
        /// </summary>
        [NameInMap("pre_rapid_upload")]
        [Validation(Required=false)]
        public bool? PreRapidUpload { get; set; }

        /// <summary>
        /// rapid_upload
        /// type: boolean
        /// </summary>
        [NameInMap("rapid_upload")]
        [Validation(Required=false)]
        public bool? RapidUpload { get; set; }

        /// <summary>
        /// upload_id
        /// </summary>
        [NameInMap("upload_id")]
        [Validation(Required=false)]
        public string UploadId { get; set; }

    }

}
