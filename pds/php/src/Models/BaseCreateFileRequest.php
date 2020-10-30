<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * create file request.
 */
class BaseCreateFileRequest extends Model
{
    /**
     * @description addition_data
     *
     * @var mixed[]
     */
    public $additionData;

    /**
     * @description ContentMd5
     *
     * @example E10ADC3949BA59ABBE56E057F20F883E
     *
     * @var string
     */
    public $contentMd5;

    /**
     * @description ContentType
     *
     * @example application/json
     *
     * @var string
     */
    public $contentType;

    /**
     * @description Name
     *
     * @example ccp.jpg
     *
     * @var string
     */
    public $name;

    /**
     * @description part_info_list
     *
     * @var UploadPartInfo[]
     */
    public $partInfoList;

    /**
     * @description Size
     *
     * @var int
     */
    public $size;

    /**
     * @description Type
     *
     * @example file
     *
     * @var string
     */
    public $type;
    protected $_name = [
        'additionData' => 'addition_data',
        'contentMd5'   => 'content_md5',
        'contentType'  => 'content_type',
        'name'         => 'name',
        'partInfoList' => 'part_info_list',
        'size'         => 'size',
        'type'         => 'type',
    ];

    public function validate()
    {
        Model::validateRequired('name', $this->name, true);
        Model::validateRequired('type', $this->type, true);
        Model::validateMaxLength('name', $this->name, 1024);
        Model::validateMinLength('name', $this->name, 1);
        Model::validateMaximum('size', $this->size, 53687091200);
        Model::validateMinimum('size', $this->size, 0);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->additionData) {
            $res['addition_data'] = $this->additionData;
        }
        if (null !== $this->contentMd5) {
            $res['content_md5'] = $this->contentMd5;
        }
        if (null !== $this->contentType) {
            $res['content_type'] = $this->contentType;
        }
        if (null !== $this->name) {
            $res['name'] = $this->name;
        }
        if (null !== $this->partInfoList) {
            $res['part_info_list'] = [];
            if (null !== $this->partInfoList && \is_array($this->partInfoList)) {
                $n = 0;
                foreach ($this->partInfoList as $item) {
                    $res['part_info_list'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->size) {
            $res['size'] = $this->size;
        }
        if (null !== $this->type) {
            $res['type'] = $this->type;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return BaseCreateFileRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['addition_data'])) {
            $model->additionData = $map['addition_data'];
        }
        if (isset($map['content_md5'])) {
            $model->contentMd5 = $map['content_md5'];
        }
        if (isset($map['content_type'])) {
            $model->contentType = $map['content_type'];
        }
        if (isset($map['name'])) {
            $model->name = $map['name'];
        }
        if (isset($map['part_info_list'])) {
            if (!empty($map['part_info_list'])) {
                $model->partInfoList = [];
                $n                   = 0;
                foreach ($map['part_info_list'] as $item) {
                    $model->partInfoList[$n++] = null !== $item ? UploadPartInfo::fromMap($item) : $item;
                }
            }
        }
        if (isset($map['size'])) {
            $model->size = $map['size'];
        }
        if (isset($map['type'])) {
            $model->type = $map['type'];
        }

        return $model;
    }
}
