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
    public class UploadPartInfo : TeaModel {
        /// <summary>
        /// etag
        /// </summary>
        [NameInMap("etag")]
        [Validation(Required=false)]
        public string Etag { get; set; }

        /// <summary>
        /// PartNumber
        /// </summary>
        [NameInMap("part_number")]
        [Validation(Required=false, Pattern="[0-9]+")]
        public long? PartNumber { get; set; }

        /// <summary>
        /// PartSize：
        /// </summary>
        [NameInMap("part_size")]
        [Validation(Required=false)]
        public long? PartSize { get; set; }

        /// <summary>
        /// upload_url
        /// </summary>
        [NameInMap("upload_url")]
        [Validation(Required=false)]
        public string UploadUrl { get; set; }

    }

}
