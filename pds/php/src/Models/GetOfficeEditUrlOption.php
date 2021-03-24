<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * GetOfficeEditUrlOption 权限控制.
 */
class GetOfficeEditUrlOption extends Model
{
    /**
     * @description Copy
     *
     * @var bool
     */
    public $copy;

    /**
     * @var bool
     */
    public $readonly;
    protected $_name = [
        'copy'     => 'copy',
        'readonly' => 'readonly',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->copy) {
            $res['copy'] = $this->copy;
        }
        if (null !== $this->readonly) {
            $res['readonly'] = $this->readonly;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetOfficeEditUrlOption
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['copy'])) {
            $model->copy = $map['copy'];
        }
        if (isset($map['readonly'])) {
            $model->readonly = $map['readonly'];
        }

        return $model;
    }
}
