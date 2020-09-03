// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * create file request
     */
    public class BaseCreateFileRequest : TeaModel {
        /// <summary>
        /// addition_data
        /// </summary>
        [NameInMap("addition_data")]
        [Validation(Required=false)]
        public Dictionary<string, object> AdditionData { get; set; }

        /// <summary>
        /// ContentMd5
        /// </summary>
        [NameInMap("content_md5")]
        [Validation(Required=false)]
        public string ContentMd5 { get; set; }

        /// <summary>
        /// ContentType
        /// </summary>
        [NameInMap("content_type")]
        [Validation(Required=false)]
        public string ContentType { get; set; }

        /// <summary>
        /// Name
        /// </summary>
        [NameInMap("name")]
        [Validation(Required=true, MaxLength=1024)]
        public string Name { get; set; }

        /// <summary>
        /// part_info_list
        /// </summary>
        [NameInMap("part_info_list")]
        [Validation(Required=false)]
        public List<UploadPartInfo> PartInfoList { get; set; }

        /// <summary>
        /// Size
        /// </summary>
        [NameInMap("size")]
        [Validation(Required=false)]
        public long Size { get; set; }

        /// <summary>
        /// Type
        /// </summary>
        [NameInMap("type")]
        [Validation(Required=true)]
        public string Type { get; set; }

    }

}
